from .base import Base
from .version_audio_files import VersionAudioFiles
from .version_game_files import VersionGameFiles
from .version_metadata import VersionMetadata


class GamePreload(Base):
    metadata: VersionMetadata
    game: VersionGameFiles
    audio: VersionAudioFiles
