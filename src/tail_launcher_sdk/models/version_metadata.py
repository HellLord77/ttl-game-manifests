from typing import Literal

from pydantic import HttpUrl

from tail_launcher_sdk.enums import DownloadMode
from tail_launcher_sdk.types_ import JsonUrl
from tail_launcher_sdk.types_ import MetadataVersion

from .base import Base
from .diff_urls import DiffUrls


class VersionMetadata(Base):
    versioned_name: str
    version: MetadataVersion
    download_mode: DownloadMode
    game_hash: Literal[""]
    index_file: Literal[""] | JsonUrl
    res_list_url: Literal[""] | HttpUrl
    diff_list_url: DiffUrls
