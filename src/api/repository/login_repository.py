from fastapi import Response

from starlette.responses import JSONResponse

from src.api.models.api_models import Login, LoginAuth
from src.api.data.data_model import Login as LoginDb

from src.utils.create_tables import create_login

from src.utils.exceptions import DataNotFound, BadRequest

from src.utils.token_util import create_access_token


class LoginRepository:
    @classmethod
    async def _login_tale(cls) -> None:
        create_login()

    @classmethod
    async def create_login(cls, login: Login) -> Response:
        await cls._login_tale()

        try:
            new_login = LoginDb.insert(**login.dict())

            new_login.execute()
        except Exception:
            raise BadRequest(
                "error: username must be unique"
            )

        return Response(
            status_code=204
        )

    @classmethod
    async def get_login(cls, login_auth: LoginAuth) -> Response:
        await cls._login_tale()

        try:
            login = LoginDb.get(
                LoginDb.username == login_auth.username,
                LoginDb.password == login_auth.password
            )
        except Exception:
            raise DataNotFound("Login Not Found")

        new_token = create_access_token({"sub": login.username})

        return JSONResponse(
            content=dict(
                id=login.id,
                play_name=login.player_name,
                username=login.username,
                access_token=new_token
            ),
        )
