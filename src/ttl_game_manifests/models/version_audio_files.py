from .base import Base
from .diff_audio_file import DiffAudioFile
from .full_audio_file import FullAudioFile


class VersionAudioFiles(Base):
    full: list[FullAudioFile]
    diff: list[DiffAudioFile]
