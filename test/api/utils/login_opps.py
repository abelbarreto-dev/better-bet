from typing import Any

from fastapi.testclient import TestClient

from src.api.routes.routes import ROUTES

from src.utils.types_utils import Token


def create_login(client: TestClient) -> Any:
    created_login = client.post(
        ROUTES["post_login"],
        json={
            "player_name": "Abel Developer",
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    return created_login


async def make_login(client: TestClient) -> Token:
    logged = client.post(
        ROUTES["post_login_auth"],
        json={
            "username": "abel_dev",
            "password": "ahjfnnjh44fuK5"
        }
    )

    content = logged.json()

    access_token = content["access_token"]

    return Token(access_token)
