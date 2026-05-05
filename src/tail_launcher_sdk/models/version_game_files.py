from .base import Base
from .diff_game_file import DiffGameFile
from .full_game_file import FullGameFile


class VersionGameFiles(Base):
    full: list[FullGameFile]
    diff: list[DiffGameFile]
