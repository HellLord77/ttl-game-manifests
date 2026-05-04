from ttl_game_manifests.types_ import JsonFileName

from .base import Base


class RepositoryManifest(Base):
    name: str
    description: str
    maintainers: list[str]
    manifests: list[JsonFileName]
