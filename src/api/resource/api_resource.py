from fastapi import APIRouter, Request
from typing import Any

from datetime import datetime

from src.api.routes.routes import ROUTES

from src.api.controller.controller import Controller

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
    return Controller.post_login(login=login)


@ROUTER.post(ROUTES["post_login_auth"])
def post_login_auth(login_auth: LoginAuth) -> Any:
    return Controller.post_login_auth(login_auth=login_auth)


@ROUTER.post(ROUTES["post_single_bet"])
def post_single_bet(single_bet: SingleBet) -> Any:
    return single_bet


@ROUTER.post(ROUTES["post_multi_bet"])
def post_multi_bet(multi_bet: MultiBet) -> Any:
    return multi_bet


@ROUTER.patch(ROUTES["patch_login_passwd"])
def patch_login_passwd(login_passwd: Request) -> Any:
    return Controller.patch_login_passwd(login_passwd=login_passwd)


@ROUTER.patch(ROUTES["patch_single_bet"])
def patch_single_bet(single_bet: Request) -> Any:
    return single_bet


@ROUTER.patch(ROUTES["patch_multi_bet"])
def patch_multi_bet(multi_bet: Request) -> Any:
    return multi_bet


@ROUTER.get(ROUTES["get_filter_single"])
def get_filter_single(date_from: datetime, date_to: datetime) -> Any:
    return None


@ROUTER.get(ROUTES["get_filter_multi"])
def get_filter_multi(date_from: datetime, date_to: datetime) -> Any:
    return None


@ROUTER.get(ROUTES["get_profits_single"])
def get_profits_single(profits_single: Request) -> Any:
    return profits_single


@ROUTER.get(ROUTES["get_profits_multi"])
def get_profits_multi(profits_multi: Request) -> Any:
    return profits_multi


@ROUTER.get(ROUTES["get_lost_single"])
def get_lost_single(lost_single: Request) -> Any:
    return lost_single


@ROUTER.get(ROUTES["get_lost_multi"])
def get_lost_multi(lost_multi: Request) -> Any:
    return lost_multi


@ROUTER.get(ROUTES["get_all_profits"])
def get_all_profits(all_profits: Request) -> Any:
    return all_profits


@ROUTER.get(ROUTES["get_all_lost"])
def get_all_lost(all_lost: Request) -> Any:
    return all_lost


@ROUTER.get(ROUTES["get_odds_success"])
def get_odds_success(odds_success: Request) -> Any:
    return odds_success


@ROUTER.post(ROUTES["post_compound_interest"])
def post_compound_interest(compound_interest: CompoundInterest) -> Any:
    return compound_interest
