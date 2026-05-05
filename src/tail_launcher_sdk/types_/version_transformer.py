import re
from typing import Annotated

from pydantic.experimental.pipeline import validate_as
from pydantic_extra_types.semantic_version import SemanticVersion

proton_version_pattern = re.compile(
    r"^(?P<major>\d+)\.(?P<minor>\d+)(?:-(?P<patch>\d+))?-proton-(?P<buildmetadata>[a-z]+)$"
)


def metadata_version_transformer(version: str) -> str:
    match version.count("."):
        case 0:
            return f"{version}.0.0"
        case 3:
            return "+".join(version.rsplit(".", 1))
        case _:
            return version


def proton_version_transformer(version: str) -> str:
    match = proton_version_pattern.match(version)
    if match is None:
        return ""

    return f"{match.group('major')}.{match.group('minor')}.{match.group('patch') or 0}+{match.group('buildmetadata')}"


MetadataVersion = Annotated[
    SemanticVersion, validate_as(str).transform(metadata_version_transformer).validate_as(SemanticVersion)
]
ProtonVersion = Annotated[
    SemanticVersion, validate_as(str).transform(proton_version_transformer).validate_as(SemanticVersion)
]
