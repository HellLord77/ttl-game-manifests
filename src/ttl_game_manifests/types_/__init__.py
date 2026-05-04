from pathlib import Path
from pathlib import PurePosixPath
from typing import Annotated

from annotated_types import Not
from annotated_types import Predicate
from pydantic import Field
from pydantic import HttpUrl

from .version_transformer import MetadataVersion as MetadataVersion
from .version_transformer import ProtonVersion as ProtonVersion

EmptyList = Annotated[list, Field(max_length=0)]
EmptyDict = Annotated[dict, Field(max_length=0)]

RelativePath = Annotated[PurePosixPath, Predicate(Not(PurePosixPath.is_absolute))]
RelativeDllPath = Annotated[RelativePath, Predicate(lambda path: path.suffix == ".dll")]
RelativeExePath = Annotated[RelativePath, Predicate(lambda path: path.suffix == ".exe")]
RelativeTxtPath = Annotated[RelativePath, Predicate(lambda path: path.suffix == ".txt")]

FileName = Annotated[Path, Predicate(lambda path: str(path.parent) == ".")]
JsonFileName = Annotated[FileName, Predicate(lambda path: path.suffix == ".json")]

IconUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith((".ico", ".png")))]
BackgroundUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith((".jpg", ".png", ".webp")))]
LiveBackgroundUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith((".mp4", ".webm")))]

JsonUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith(".json"))]

HexMd5 = Annotated[str, Field(pattern=r"^[a-fA-F0-9]{32}$")]
