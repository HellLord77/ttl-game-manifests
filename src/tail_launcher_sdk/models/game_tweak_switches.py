from typing import Literal

from .base import Base


class GameTweakSwitches(Base):
    fps_unlocker: bool
    jadeite: Literal[False]
    xxmi: bool
    graphics_api: bool
