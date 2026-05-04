from typing import Literal

from ttl_game_manifests.types_ import BackgroundUrl
from ttl_game_manifests.types_ import IconUrl
from ttl_game_manifests.types_ import LiveBackgroundUrl

from .base import Base


class VersionAssets(Base):
    game_icon: IconUrl
    game_background: BackgroundUrl
    game_live_background: Literal[""] | LiveBackgroundUrl
