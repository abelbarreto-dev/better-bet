from src.utils.create_tables import drop_all_tables

from fastapi.testclient import TestClient

from test.mock.data_mock import DATA

from src.api.routes.routes import ROUTES


def test_post_login_success(client: TestClient) -> None:
    created_login = client.post(
        ROUTES["post_login"],
        json=DATA["login"]
    )

    assert created_login.status_code == 204

    drop_all_tables()


def test_post_login_failure_empty_json(client: TestClient) -> None:
    created_login = client.post(
        ROUTES["post_login"],
        json={}
    )

    assert created_login.status_code == 422

    drop_all_tables()


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

    drop_all_tables()
