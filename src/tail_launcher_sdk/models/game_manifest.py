from typing import Literal

from tail_launcher_sdk.enums import GameBiz
from tail_launcher_sdk.types_ import MetadataVersion

from .base import Base
from .game_extras import GameExtras
from .game_paths import GamePaths
from .game_version import GameVersion
from .version_assets import VersionAssets


class GameManifest(Base):
    version: Literal[1]
    display_name: str
    biz: GameBiz
    latest_version: MetadataVersion
    game_versions: list[GameVersion]
    telemetry_hosts: list[str]
    paths: GamePaths
    assets: VersionAssets
    extra: GameExtras

    def find_game_version(self, metadata_version: str | MetadataVersion) -> GameVersion | None:
        for game_version in self.game_versions:
            if metadata_version == game_version.metadata.version:
                return game_version
        return None

    def get_latest_game_version(self) -> GameVersion:
        game_version = self.find_game_version(self.latest_version)
        assert game_version is not None  # noqa: S101
        return game_version
