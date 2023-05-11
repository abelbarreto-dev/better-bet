from fastapi import APIRouter
from typing import Any

from src.api.routes.routes import ROUTES

from src.api.models.api_models import (
    Login,
    LoginAuth,
    SingleBet,
    MultiBet,
    CompoundInterest
)


ROUTER = APIRouter()


@ROUTER.post(ROUTES["post_login"])
def post_login(login: Login) -> Any:
    return login


@ROUTER.post(ROUTES["post_login_auth"])
def post_login_auth(login_auth: LoginAuth) -> Any:
    return login_auth


@ROUTER.post(ROUTES["post_single_bet"])
def post_single_bet(single_bet: SingleBet) -> Any:
    return single_bet


@ROUTER.post(ROUTES["post_multi_bet"])
def post_multi_bet(multi_bet: MultiBet) -> Any:
    return multi_bet
