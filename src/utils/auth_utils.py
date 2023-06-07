from typing import Any

from jose import JWTError

from fastapi import (
    Depends,
    HTTPException,
    status,
)

from fastapi.security import OAuth2PasswordBearer

from src.api.data.data_model import Login

from src.utils.token_util import check_access_token
from src.utils.types_utils import Token


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


async def get_logged_user(token: Token = Depends(oauth2_schema)) -> Any:
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        username = check_access_token(token)
    except JWTError:
        raise exception

    if not username:
        raise exception

    login = Login.get(Login.username == username)

    if not login:
        raise exception

    return dict(
        id=login.id,
        player_name=login.player_name,
        username=login.username,
    )
