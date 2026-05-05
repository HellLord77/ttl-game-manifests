from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl

from tail_launcher_sdk.enums import DiffType
from tail_launcher_sdk.types_ import EmptyList
from tail_launcher_sdk.types_ import HexMd5
from tail_launcher_sdk.types_ import MetadataVersion

from .base import Base


class DiffGameFile(Base):
    file_url: HttpUrl
    compressed_size: Literal[""] | ByteSize
    decompressed_size: Literal[""] | ByteSize
    file_hash: Literal[""] | HexMd5
    file_path: Literal[""] | HttpUrl
    diff_type: DiffType
    original_version: MetadataVersion
    delete_files: EmptyList
