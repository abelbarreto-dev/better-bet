import pytest

from typing import Generator

from fastapi.testclient import TestClient

from set_config import to_testing
from src.api.app.app import better_bet_api


@pytest.fixture(scope="function")
def client() -> Generator:
    to_testing()

    with TestClient(better_bet_api) as testing:
        yield testing
