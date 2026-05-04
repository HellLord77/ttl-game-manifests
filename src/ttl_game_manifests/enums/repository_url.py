from enum import Enum

from httpx import URL


class RepositoryUrl(URL, Enum):
    OFFICIAL = "https://raw.githubusercontent.com/TwintailTeam/game-manifests/HEAD/"
    OFFICIAL_MAIN = "https://raw.githubusercontent.com/TwintailTeam/game-manifests/refs/heads/main/"
    OFFICIAL_NEXT = "https://raw.githubusercontent.com/TwintailTeam/game-manifests/refs/heads/next/"
