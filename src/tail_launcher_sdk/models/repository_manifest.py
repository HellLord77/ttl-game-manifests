from tail_launcher_sdk.types_ import JsonFileName

from .base import Base


class RepositoryManifest(Base):
    name: str
    description: str
    maintainers: list[str]
    manifests: list[JsonFileName]
