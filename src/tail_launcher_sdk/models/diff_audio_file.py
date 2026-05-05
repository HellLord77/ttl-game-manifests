from typing import Literal

from pydantic import ByteSize
from pydantic import HttpUrl
from pydantic_extra_types.semantic_version import SemanticVersion

from tail_launcher_sdk.enums import DiffType
from tail_launcher_sdk.enums import Language
from tail_launcher_sdk.types_ import HexMd5

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
