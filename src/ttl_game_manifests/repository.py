from typing import override

from httpx import AsyncClient
from httpx import Client

from .enums import GameBiz
from .enums import RepositoryUrl
from .models import GameManifest
from .models import RepositoryManifest
from .models.base import Base
from .models.game_version import GameVersion
from .types_ import MetadataVersion


class Repository:
    def __init__(self, url: RepositoryUrl = RepositoryUrl.OFFICIAL_MAIN, *, client: Client | None = None) -> None:
        self.url = url

        if client is None:
            client = Client()
        self.client = client

    def _get_model[T: Base](self, path: str, *, model: type[T]) -> T:
        url = self.url.join(path)
        response = self.client.get(url)

        response.raise_for_status()
        return model.model_validate_json(response.content)

    def get_repository_manifest(self) -> RepositoryManifest:
        return self._get_model("repository.json", model=RepositoryManifest)

    def get_game_manifest(self, game_biz: GameBiz) -> GameManifest:
        return self._get_model(f"{game_biz}.json", model=GameManifest)

    @classmethod
    def get_latest_game_version(cls, game_manifest: GameManifest) -> GameVersion:
        game_version = cls.find_game_version(game_manifest, game_manifest.latest_version)
        if game_version is None:
            raise NotImplementedError
        return game_version

    @staticmethod
    def find_game_version(game_manifest: GameManifest, metadata_version: MetadataVersion) -> GameVersion | None:
        for game_version in game_manifest.game_versions:
            if metadata_version == game_version.metadata.version:
                return game_version
        return None


class AsyncRepository(Repository):
    def __init__(self, url: RepositoryUrl = RepositoryUrl.OFFICIAL_MAIN, *, client: AsyncClient | None = None) -> None:
        if client is None:
            client = AsyncClient()

        super().__init__(url, client=client)

    @override
    async def _get_model[T: Base](self, path: str, *, model: type[T]) -> T:
        url = self.url.join(path)
        response = await self.client.get(url)

        response.raise_for_status()
        return model.model_validate_json(response.content)
