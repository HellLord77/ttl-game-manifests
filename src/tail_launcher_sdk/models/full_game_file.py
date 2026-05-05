from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl

from tail_launcher_sdk.enums import RegionCode
from tail_launcher_sdk.types_ import HexMd5

from .base import Base


class FullGameFile(Base):
    file_url: HttpUrl
    compressed_size: ByteSize
    decompressed_size: ByteSize
    file_hash: Literal[""] | HexMd5
    file_path: Literal[""] | HttpUrl
    region_code: Literal[""] | RegionCode
