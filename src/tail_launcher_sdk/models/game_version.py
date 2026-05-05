from .base import Base
from .version_assets import VersionAssets
from .version_audio_files import VersionAudioFiles
from .version_game_files import VersionGameFiles
from .version_metadata import VersionMetadata


class GameVersion(Base):
    metadata: VersionMetadata
    assets: VersionAssets
    game: VersionGameFiles
    audio: VersionAudioFiles
