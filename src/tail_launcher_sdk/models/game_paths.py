from typing import Literal

from tail_launcher_sdk.enums import DirType
from tail_launcher_sdk.types_ import RelativeExePath
from tail_launcher_sdk.types_ import RelativePath

from .base import Base


class GamePaths(Base):
    audio_pkg_res_dir: RelativePath
    exe_filename: RelativeExePath
    installation_dir: RelativePath
    screenshot_dir: RelativePath
    screenshot_dir_relative_to: Literal[""] | DirType
