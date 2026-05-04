import pytest

pytestmark = [pytest.mark.vcr]


@pytest.fixture(scope="module")
def repository():
    from ttl_game_manifests import Repository

    return Repository()


def test_repository_manifest(repository):
    from ttl_game_manifests.models import RepositoryManifest

    repository_manifest = repository.get_repository_manifest()
    assert isinstance(repository_manifest, RepositoryManifest)


def test_game_manifest(game_biz, repository):
    from ttl_game_manifests.models import GameManifest

    game_manifest = repository.get_game_manifest(game_biz)
    assert isinstance(game_manifest, GameManifest)
