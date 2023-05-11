from typing import Any

from src.api.models.api_models import (
    Login,
    LoginAuth
)


class Controller:

    @classmethod
    def post_login(cls, login: Login) -> Any:
        return cls

    @classmethod
    def post_login_auth(cls, login_auth: LoginAuth) -> Any:
        return cls

    @classmethod
    def patch_login_passwd(cls, login_passwd: Any) -> Any:
        return cls
