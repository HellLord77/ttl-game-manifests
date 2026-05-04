from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl

from ttl_game_manifests.enums import Language
from ttl_game_manifests.types_ import HexMd5

from .base import Base


class FullAudioFile(Base):
    file_url: HttpUrl
    compressed_size: ByteSize
    decompressed_size: ByteSize
    file_hash: HexMd5
    file_path: Literal[""] | HttpUrl
    language: Language
    region_code: Literal[""]
