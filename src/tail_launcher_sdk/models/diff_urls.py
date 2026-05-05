from typing import Literal

from pydantic import HttpUrl

from .base import Base


class DiffUrls(Base):
    game: Literal[""] | HttpUrl
    en_us: Literal[""] | HttpUrl
    zh_cn: Literal[""] | HttpUrl
    ja_jp: Literal[""] | HttpUrl
    ko_kr: Literal[""] | HttpUrl
