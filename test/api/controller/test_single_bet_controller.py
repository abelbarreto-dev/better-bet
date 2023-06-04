from src.api.data.data_model import Login

from src.utils.create_tables import drop_all_tables

from fastapi.testclient import TestClient

from src.api.routes.routes import ROUTES

from src.utils.types_utils import get_datetime_brazil


def test_post_single_bet_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    created_single_bet = client.post(
        ROUTES["post_single_bet"],
        json={
            "id_login": 1,
            "odd": "1.25",
            "value_invest": "250.00",
            "description": "+0.5 goals",
            "home_team": "Liverpool",
            "away_team": "Manchester City",
            "team_bet": None,
            "operator_fee": "0.065"
        }
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204

    drop_all_tables()


def test_post_single_bet_failure(client: TestClient) -> None:
    drop_all_tables()

    Login.create_table()

    created_single_bet = client.post(
        ROUTES["post_single_bet"],
        json={
            "id_login_id": 1,
            "odd": "1.25",
            "value_invest": "250.00",
            "description": "+0.5 goals",
            "home_team": "Liverpool",
            "away_team": "Manchester City",
            "team_bet": None,
            "operator_fee": "0.065"
        }
    )

    assert created_single_bet.status_code == 422

    drop_all_tables()


def test_post_single_bet_checker_failure(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    created_single_bet = client.post(
        ROUTES["post_single_bet"],
        json={
            "id_login": 1,
            "odd": "-1.25",
            "value_invest": "250.00",
            "description": "+0.5 goals",
            "home_team": "Liverpool",
            "away_team": "Manchester City",
            "team_bet": None,
            "operator_fee": "0.065"
        }
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 400

    drop_all_tables()


def test_patch_single_bet_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    created_single_bet = client.post(
        ROUTES["post_single_bet"],
        json={
            "id_login": 1,
            "odd": "1.25",
            "value_invest": "250.00",
            "description": "+0.5 goals",
            "home_team": "Liverpool",
            "away_team": "Manchester City",
            "team_bet": None,
            "operator_fee": "0.065"
        }
    )

    patch_single_bet = client.patch(
        ROUTES["patch_single_bet"],
        json={
            "id": 1,
            "bet_status": "success"
        }
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204
    assert patch_single_bet.status_code == 204

    drop_all_tables()


def test_patch_single_bet_failure(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    created_single_bet = client.post(
        ROUTES["post_single_bet"],
        json={
            "id_login": 1,
            "odd": "1.25",
            "value_invest": "250.00",
            "description": "+0.5 goals",
            "home_team": "Liverpool",
            "away_team": "Manchester City",
            "team_bet": None,
            "operator_fee": "0.065"
        }
    )

    patch_single_bet = client.patch(
        ROUTES["patch_single_bet"],
        json={
            "id": 2,
            "bet_status": "success"
        }
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204
    assert patch_single_bet.status_code == 404
    assert patch_single_bet.json() == {
        "detail": {
            "message": "error: SingleBet Not Found"
        }
    }

    drop_all_tables()


def test_get_filter_single_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    created_single_bet = client.post(
        ROUTES["post_single_bet"],
        json={
            "id_login": 1,
            "odd": "1.25",
            "value_invest": "250.00",
            "description": "+0.5 goals",
            "home_team": "Liverpool",
            "away_team": "Manchester City",
            "team_bet": None,
            "operator_fee": "0.065"
        }
    )

    brazil_date = str(get_datetime_brazil().date())

    get_single_bet = client.post(
        ROUTES["get_filter_single"],
        json={
            "login_id": 1,
            "date_from": brazil_date,
            "date_to": brazil_date
        }
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204
    assert get_single_bet.status_code == 200

    drop_all_tables()


def test_get_filter_single_failure(client: TestClient) -> None:
    drop_all_tables()

    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    created_single_bet = client.post(
        ROUTES["post_single_bet"],
        json={
            "id_login": 1,
            "odd": "1.25",
            "value_invest": "250.00",
            "description": "+0.5 goals",
            "home_team": "Liverpool",
            "away_team": "Manchester City",
            "team_bet": None,
            "operator_fee": "0.065"
        }
    )

    brazil_date = str(get_datetime_brazil().date())

    get_single_bet = client.post(
        ROUTES["get_filter_single"],
        json={
            "login_id": 2,
            "date_from": brazil_date,
            "date_to": brazil_date
        }
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204
    assert get_single_bet.status_code == 404

    drop_all_tables()
