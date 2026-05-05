from typing import Literal

from tail_launcher_sdk.enums import ProtonCompatConfig
from tail_launcher_sdk.enums import WinetricksVerb
from tail_launcher_sdk.types_ import ProtonVersion

from .base import Base
from .compat_platform_overrides import CompatPlatformOverrides


class GameCompatOverrides(Base):
    install_to_prefix: Literal[False]
    disable_protonfixes: Literal[True]
    protonfixes_id: Literal[""]
    protonfixes_store: Literal[""]
    stub_wintrust: bool
    block_first_req: bool
    proton_compat_config: list[ProtonCompatConfig]
    override_runner: CompatPlatformOverrides
    min_runner_versions: list[ProtonVersion]
    winetricks_verbs: list[WinetricksVerb]
