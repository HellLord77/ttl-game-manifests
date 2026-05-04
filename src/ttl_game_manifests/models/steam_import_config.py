from typing import Literal

from ttl_game_manifests.types_ import RelativeDllPath
from ttl_game_manifests.types_ import RelativeTxtPath

from .base import Base


class SteamImportConfig(Base):
    enabled: bool
    steam_appid_txt: Literal[""] | RelativeTxtPath
    steam_api_dll: Literal[""] | RelativeDllPath
