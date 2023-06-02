import pytest

from typing import Generator

from fastapi.testclient import TestClient

from set_config import to_testing

from main import app


@pytest.fixture(scope="function")
def client() -> Generator:
    to_testing()

    with TestClient(app) as testing:
        yield testing
