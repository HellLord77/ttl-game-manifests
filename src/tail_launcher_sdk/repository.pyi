from collections.abc import Awaitable

from httpx import AsyncClient
from httpx import Client

from .enums import GameBiz
from .enums import RepositoryUrl
from .models import GameManifest
from .models import RepositoryManifest
from .models.base import Base

class Repository:
    url: RepositoryUrl
    client: Client

    def __init__(self, url: str | RepositoryUrl = ..., *, client: Client | None = None) -> None: ...
    def _get_model[T: Base](self, path: str, *, model: type[T]) -> T: ...
    def get_repository_manifest(self) -> RepositoryManifest: ...
    def get_game_manifest(self, game_biz: GameBiz) -> GameManifest: ...

class AsyncRepository(Repository):
    client: AsyncClient

    def __init__(self, url: str | RepositoryUrl = ..., *, client: AsyncClient | None = None) -> None: ...
    async def _get_model[T: Base](self, path: str, *, model: type[T]) -> T: ...
    def get_repository_manifest(self) -> Awaitable[RepositoryManifest]: ...
    def get_game_manifest(self, game_biz: GameBiz) -> Awaitable[GameManifest]: ...
