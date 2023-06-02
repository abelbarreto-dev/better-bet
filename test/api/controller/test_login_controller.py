from set_config import to_staging

from fastapi.testclient import TestClient

from test.mock.data_mock import DATA

from src.api.routes.routes import ROUTES

from src.api.data.data_model import Login, SingleBet, MultiBet


def drop_login_table() -> None:
    SingleBet.drop_table()
    MultiBet.drop_table()
    Login.drop_table()
    to_staging()


def test_post_login_success(client: TestClient) -> None:
    created_login = client.post(
        ROUTES["post_login"],
        json=DATA["login"]
    )

    assert created_login.status_code == 204
    drop_login_table()


def test_post_login_failure_empty_json(client: TestClient) -> None:
    created_login = client.post(
        ROUTES["post_login"],
        json={}
    )

    assert created_login.status_code == 422

    drop_login_table()


def test_post_login_failure_existing_login(client: TestClient) -> None:
    created_login = client.post(
        ROUTES["post_login"],
        json=DATA["login"]
    )

    created_login = client.post(
        ROUTES["post_login"],
        json=DATA["login"]
    )

    assert created_login.status_code == 400
    assert created_login.json() == {
        "detail": {
            "message": "error: username must be unique"
        }
    }

    drop_login_table()
