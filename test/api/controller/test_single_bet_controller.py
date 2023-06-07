import pytest

from src.utils.create_tables import drop_all_tables

from fastapi.testclient import TestClient

from src.api.routes.routes import ROUTES

from src.utils.types_utils import (
    get_datetime_brazil,
    Token,
)

from test.api.utils.login_opps import (
    create_login,
    make_login,
)

from test.api.utils.get_auth_headers import headers_acc_tk


@pytest.mark.asyncio
async def test_post_single_bet_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = create_login(client)
    access_token = await make_login(client)

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
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204

    drop_all_tables()


@pytest.mark.asyncio
async def test_post_single_bet_checker_failure(client: TestClient) -> None:
    drop_all_tables()

    created_login = create_login(client)
    access_token = await make_login(client)

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
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 400

    drop_all_tables()


@pytest.mark.asyncio
async def test_patch_single_bet_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = create_login(client)
    access_token = await make_login(client)

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
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    patch_single_bet = client.patch(
        ROUTES["patch_single_bet"],
        json={
            "id": 1,
            "bet_status": "success"
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204
    assert patch_single_bet.status_code == 204

    drop_all_tables()


@pytest.mark.asyncio
async def test_patch_single_bet_failure(client: TestClient) -> None:
    drop_all_tables()

    created_login = create_login(client)
    access_token = await make_login(client)

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
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    patch_single_bet = client.patch(
        ROUTES["patch_single_bet"],
        json={
            "id": 2,
            "bet_status": "success"
        },
        headers=headers_acc_tk(Token(access_token)),
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


@pytest.mark.asyncio
async def test_get_filter_single_success(client: TestClient) -> None:
    drop_all_tables()

    created_login = create_login(client)
    access_token = await make_login(client)

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
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    brazil_date = str(get_datetime_brazil().date())

    get_single_bet = client.post(
        ROUTES["get_filter_single"],
        json={
            "login_id": 1,
            "date_from": brazil_date,
            "date_to": brazil_date
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204
    assert get_single_bet.status_code == 200

    drop_all_tables()


@pytest.mark.asyncio
async def test_get_filter_single_failure(client: TestClient) -> None:
    drop_all_tables()

    created_login = create_login(client)
    access_token = await make_login(client)

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
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    brazil_date = str(get_datetime_brazil().date())

    get_single_bet = client.post(
        ROUTES["get_filter_single"],
        json={
            "login_id": 2,
            "date_from": brazil_date,
            "date_to": brazil_date
        },
        headers=headers_acc_tk(Token(access_token)),
    )

    assert created_login.status_code == 204
    assert created_single_bet.status_code == 204
    assert get_single_bet.status_code == 404

    drop_all_tables()
