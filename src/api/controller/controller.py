from fastapi import (
    APIRouter,
    Request,
    Depends,
)

from typing import Any

from src.api.routes.routes import ROUTES

from src.api.application.application import Controller

from src.utils.auth_utils import get_logged_user

from src.api.models.api_models import (
    Login,
    LoginAuth,
    SingleBet,
    MultiBet,
    CompoundInterest,
)

from src.api.data.data_model import Login as LoginDB


ROUTER = APIRouter()


@ROUTER.get(ROUTES["me"])
async def me(login_db: LoginDB = Depends(get_logged_user)) -> Any:
    return login_db


@ROUTER.post(ROUTES["post_login"])
async def post_login(login: Login) -> Any:
    return await Controller.post_login(login)


@ROUTER.post(ROUTES["post_login_auth"])
async def post_login_auth(login_auth: LoginAuth) -> Any:
    return await Controller.post_login_auth(login_auth)


@ROUTER.post(ROUTES["post_single_bet"])
async def post_single_bet(
    single_bet: SingleBet,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.post_single_bet(single_bet)


@ROUTER.post(ROUTES["post_multi_bet"])
async def post_multi_bet(
    multi_bet: MultiBet,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.post_multi_bet(multi_bet)


@ROUTER.patch(ROUTES["patch_single_bet"])
async def patch_single_bet(
    single_bet: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.patch_single_bet(single_bet)


@ROUTER.patch(ROUTES["patch_multi_bet"])
async def patch_multi_bet(
    multi_bet: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.patch_multi_bet(multi_bet)


@ROUTER.post(ROUTES["get_filter_single"])
async def get_filter_single(
    date_filter: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_filter_single(date_filter)


@ROUTER.post(ROUTES["get_filter_multi"])
async def get_filter_multi(
    date_filter: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_filter_multi(date_filter)


@ROUTER.post(ROUTES["get_profits_single"])
async def get_profits_single(
    profits_single: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_profits_single(profits_single)


@ROUTER.post(ROUTES["get_profits_multi"])
async def get_profits_multi(
    profits_multi: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_profits_multi(profits_multi)


@ROUTER.post(ROUTES["get_lost_single"])
async def get_lost_single(
    lost_single: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_lost_single(lost_single)


@ROUTER.post(ROUTES["get_lost_multi"])
async def get_lost_multi(
    lost_multi: Request,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_lost_multi(lost_multi)


@ROUTER.get(ROUTES["get_all_profits"])
async def get_all_profits(
    id_login: int,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_all_profits(id_login)


@ROUTER.get(ROUTES["get_all_lost"])
async def get_all_lost(
    id_login: int,
    login_db: LoginDB = Depends(get_logged_user)
) -> Any:
    return await Controller.get_all_lost(id_login)


@ROUTER.post(ROUTES["post_compound_interest"])
async def post_compound_interest(compound_interest: CompoundInterest) -> Any:
    return await Controller.post_compound_interest(compound_interest)
