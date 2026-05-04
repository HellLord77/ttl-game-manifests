from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl
from pydantic_extra_types.semantic_version import SemanticVersion

from ttl_game_manifests.enums import DiffType
from ttl_game_manifests.enums import Language
from ttl_game_manifests.types_ import HexMd5

from .base import Base


class DiffAudioFile(Base):
    file_url: HttpUrl
    compressed_size: Literal[""] | ByteSize
    decompressed_size: Literal[""] | ByteSize
    file_hash: Literal[""] | HexMd5
    file_path: Literal[""] | HttpUrl
    diff_type: DiffType
    original_version: SemanticVersion
    language: Language
