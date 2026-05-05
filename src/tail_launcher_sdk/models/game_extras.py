from tail_launcher_sdk.types_ import EmptyDict

from .base import Base
from .game_compat_overrides import GameCompatOverrides
from .game_preload import GamePreload
from .game_tweak_switches import GameTweakSwitches
from .graphics_api_config import GraphicsApiConfig
from .steam_import_config import SteamImportConfig


class GameExtras(Base):
    preload: EmptyDict | GamePreload
    switches: GameTweakSwitches
    compat_overrides: GameCompatOverrides
    fps_unlock_options: list[int]
    steam_import_config: SteamImportConfig
    graphics_api_options: GraphicsApiConfig
