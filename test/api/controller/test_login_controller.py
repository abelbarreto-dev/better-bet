from src.utils.create_tables import drop_all_tables

from fastapi.testclient import TestClient

from src.api.routes.routes import ROUTES


def test_post_login_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    assert created_login.status_code == 204


def test_post_login_failure_empty_json(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={}
    )

    assert created_login.status_code == 422


def test_post_login_failure_existing_login(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    assert created_login.status_code == 400
    assert created_login.json() == {
        "detail": {
            "message": "error: username must be unique"
        }
    }


def test_login_checker_failure(client: TestClient) -> None:
    drop_all_tables()

    invalid_login = {
        "player_name": "Abel Developer",
        "username": "abel_dev",
        "password": " passwfjagfne4j3"
    }

    created_login = client.post(
        ROUTES["post_login"],
        json=invalid_login
    )

    assert created_login.status_code == 400


def test_login_auth_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    make_login = client.post(
        ROUTES["post_login_auth"],
        json={
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    assert created_login.status_code == 204
    assert make_login.status_code == 200


def test_login_auth_failure_checker(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    login_auth = {
        "username": "abel_dev",
        "password": " adnfjn44i49jf"
    }

    make_login = client.post(
        ROUTES["post_login_auth"],
        json=login_auth
    )

    assert created_login.status_code == 204
    assert make_login.status_code == 400


def test_login_auth_failure(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    login_auth = {
        "username": "abel_dev",
        "password": "adnfjn44i49jf"
    }

    make_login = client.post(
        ROUTES["post_login_auth"],
        json=login_auth
    )

    assert created_login.status_code == 204
    assert make_login.status_code == 404
