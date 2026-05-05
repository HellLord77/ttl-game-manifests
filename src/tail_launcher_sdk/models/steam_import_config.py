from typing import Literal

from tail_launcher_sdk.types_ import RelativeDllPath
from tail_launcher_sdk.types_ import RelativeTxtPath

from .base import Base


class SteamImportConfig(Base):
    enabled: bool
    steam_appid_txt: Literal[""] | RelativeTxtPath
    steam_api_dll: Literal[""] | RelativeDllPath
