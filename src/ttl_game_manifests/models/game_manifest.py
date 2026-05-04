from typing import Literal

from ttl_game_manifests.enums import GameBiz
from ttl_game_manifests.types_ import MetadataVersion

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
