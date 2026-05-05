from typing import Literal

from tail_launcher_sdk.types_ import BackgroundUrl
from tail_launcher_sdk.types_ import IconUrl
from tail_launcher_sdk.types_ import LiveBackgroundUrl

from .base import Base


class VersionAssets(Base):
    game_icon: IconUrl
    game_background: BackgroundUrl
    game_live_background: Literal[""] | LiveBackgroundUrl
