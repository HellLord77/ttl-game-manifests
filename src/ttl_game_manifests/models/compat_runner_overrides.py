from typing import Literal

from ttl_game_manifests.types_ import ProtonVersion

from .base import Base


class CompatRunnerOverrides(Base):
    enabled: bool
    runner_version: Literal[""] | ProtonVersion
