from typing import Any, Dict

from json import loads

from fastapi import Request

from src.api.models.api_models import (
    Login,
    LoginAuth,
    SingleBet,
    MultiBet,
)

from src.utils.exceptions import (
    BadRequest
)

from src.utils.checker import (
    create_login_checker,
    login_auth_checker,
    single_bet_checker,
    multi_bet_checker
)


class Controller:

    @classmethod
    async def _get_data_from_request(cls, request: Request) -> Dict[str, Any]:
        data_json = await request.body()

        data_json = data_json.decode("utf-8")

        data_dict = loads(data_json)

        return data_dict

    @classmethod
    async def post_login(cls, login: Login) -> Any:
        try:
            create_login_checker(login)
        except ValueError as ve:
            raise BadRequest(ve.args[0])

    @classmethod
    async def post_login_auth(cls, login_auth: LoginAuth) -> Any:
        try:
            login_auth_checker(login_auth)
        except ValueError as ve:
            raise BadRequest(ve.args[0])

    @classmethod
    async def post_single_bet(cls, single_bet: SingleBet) -> Any:
        try:
            single_bet_checker(single_bet)
        except ValueError as ve:
            raise BadRequest(ve.args[0])

    @classmethod
    async def post_multi_bet(cls, multi_bet: MultiBet) -> Any:
        try:
            multi_bet_checker(multi_bet)
        except ValueError as ve:
            raise BadRequest(ve.args[0])

    @classmethod
    async def patch_single_bet(cls, single_bet: Request) -> Any:
        return single_bet

    @classmethod
    async def patch_multi_bet(cls, multi_bet: Request) -> Any:
        return multi_bet
