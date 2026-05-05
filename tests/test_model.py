from pathlib import Path

import pytest


@pytest.fixture
def json_data(request: pytest.FixtureRequest, datadir: Path) -> bytes:
    path = datadir / f"{request.node.name}.json"
    return path.read_bytes()


def test_game_manifest(json_data):
    from tail_launcher_sdk.models import GameManifest

    game_manifest = GameManifest.model_validate_json(json_data)
    assert isinstance(game_manifest, GameManifest)


def test_repository_manifest(json_data):
    from tail_launcher_sdk.models import RepositoryManifest

    repository_manifest = RepositoryManifest.model_validate_json(json_data)
    assert isinstance(repository_manifest, RepositoryManifest)
