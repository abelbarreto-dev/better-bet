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
async def post_login(login: Login) -> Any:
    return await Controller.post_login(login)


@ROUTER.post(ROUTES["post_login_auth"])
async def post_login_auth(login_auth: LoginAuth) -> Any:
    return await Controller.post_login_auth(login_auth)


@ROUTER.post(ROUTES["post_single_bet"])
async def post_single_bet(single_bet: SingleBet) -> Any:
    return await Controller.post_single_bet(single_bet)


@ROUTER.post(ROUTES["post_multi_bet"])
async def post_multi_bet(multi_bet: MultiBet) -> Any:
    return await Controller.post_multi_bet(multi_bet)


@ROUTER.patch(ROUTES["patch_single_bet"])
async def patch_single_bet(single_bet: Request) -> Any:
    return await Controller.patch_single_bet(single_bet)


@ROUTER.patch(ROUTES["patch_multi_bet"])
async def patch_multi_bet(multi_bet: Request) -> Any:
    return await Controller.patch_multi_bet(multi_bet)


@ROUTER.get(ROUTES["get_filter_single"])
async def get_filter_single(date_filer: Request) -> Any:
    return None


@ROUTER.get(ROUTES["get_filter_multi"])
async def get_filter_multi(date_filer: Request) -> Any:
    return None


@ROUTER.get(ROUTES["get_profits_single"])
async def get_profits_single(profits_single: Request) -> Any:
    return profits_single


@ROUTER.get(ROUTES["get_profits_multi"])
async def get_profits_multi(profits_multi: Request) -> Any:
    return profits_multi


@ROUTER.get(ROUTES["get_lost_single"])
async def get_lost_single(lost_single: Request) -> Any:
    return lost_single


@ROUTER.get(ROUTES["get_lost_multi"])
async def get_lost_multi(lost_multi: Request) -> Any:
    return lost_multi


@ROUTER.get(ROUTES["get_all_profits"])
async def get_all_profits(all_profits: Request) -> Any:
    return all_profits


@ROUTER.get(ROUTES["get_all_lost"])
async def get_all_lost(all_lost: Request) -> Any:
    return all_lost


@ROUTER.get(ROUTES["get_odds_success"])
async def get_odds_success(odds_success: Request) -> Any:
    return odds_success


@ROUTER.post(ROUTES["post_compound_interest"])
async def post_compound_interest(compound_interest: CompoundInterest) -> Any:
    return await Controller.post_compound_interest(compound_interest)
