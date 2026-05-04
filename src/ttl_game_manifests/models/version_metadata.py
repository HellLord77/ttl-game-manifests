from typing import Literal

from pydantic import HttpUrl

from ttl_game_manifests.enums import DownloadMode
from ttl_game_manifests.types_ import JsonUrl
from ttl_game_manifests.types_ import MetadataVersion

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
