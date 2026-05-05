import pytest

pytestmark = [pytest.mark.anyio, pytest.mark.vcr]


@pytest.fixture(scope="module")
def repository():
    from tail_launcher_sdk import AsyncRepository

    return AsyncRepository()


async def test_repository_manifest(repository):
    from tail_launcher_sdk.models import RepositoryManifest

    repository_manifest = await repository.get_repository_manifest()
    assert isinstance(repository_manifest, RepositoryManifest)


async def test_game_manifest(repository):
    from tail_launcher_sdk import GameBiz
    from tail_launcher_sdk.models import GameManifest

    game_manifest = await repository.get_game_manifest(GameBiz.HK4E)
    assert isinstance(game_manifest, GameManifest)
