from typing import Literal

from ttl_game_manifests.enums import DirType
from ttl_game_manifests.types_ import RelativeExePath
from ttl_game_manifests.types_ import RelativePath

from .base import Base


class GamePaths(Base):
    audio_pkg_res_dir: RelativePath
    exe_filename: RelativeExePath
    installation_dir: RelativePath
    screenshot_dir: RelativePath
    screenshot_dir_relative_to: Literal[""] | DirType
