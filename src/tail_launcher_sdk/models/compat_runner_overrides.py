from typing import Literal

from tail_launcher_sdk.types_ import ProtonVersion

from .base import Base


class CompatRunnerOverrides(Base):
    enabled: bool
    runner_version: Literal[""] | ProtonVersion
