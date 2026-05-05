import pytest

pytestmark = [pytest.mark.vcr]


@pytest.fixture(scope="module")
def repository():
    from tail_launcher_sdk import Repository

    return Repository()


def test_repository_manifest(repository):
    from tail_launcher_sdk.models import RepositoryManifest

    repository_manifest = repository.get_repository_manifest()
    assert isinstance(repository_manifest, RepositoryManifest)


def test_game_manifest(game_biz, repository):
    from tail_launcher_sdk.models import GameManifest

    game_manifest = repository.get_game_manifest(game_biz)
    assert isinstance(game_manifest, GameManifest)
