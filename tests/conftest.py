import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc: pytest.Metafunc):
    from tail_launcher_sdk import GameBiz

    if "game_biz" in metafunc.fixturenames:
        game_biz = GameBiz if metafunc.config.getoption("--all") else (GameBiz.HK4E,)
        metafunc.parametrize("game_biz", game_biz, scope="module")
