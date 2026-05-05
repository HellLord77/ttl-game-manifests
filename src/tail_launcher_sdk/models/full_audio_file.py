from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl

from tail_launcher_sdk.enums import Language
from tail_launcher_sdk.types_ import HexMd5

from .base import Base


class FullAudioFile(Base):
    file_url: HttpUrl
    compressed_size: ByteSize
    decompressed_size: ByteSize
    file_hash: HexMd5
    file_path: Literal[""] | HttpUrl
    language: Language
    region_code: Literal[""]
