from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl

from ttl_game_manifests.enums import DiffType
from ttl_game_manifests.types_ import EmptyList
from ttl_game_manifests.types_ import HexMd5
from ttl_game_manifests.types_ import MetadataVersion

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
