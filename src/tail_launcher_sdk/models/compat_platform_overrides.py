from .base import Base
from .compat_runner_overrides import CompatRunnerOverrides


class CompatPlatformOverrides(Base):
    linux: CompatRunnerOverrides
    macos: CompatRunnerOverrides
