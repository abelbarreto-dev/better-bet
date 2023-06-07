from typing import (
    Dict,
    Any,
)

from src.utils.types_utils import Token


def headers_acc_tk(access_token: Token) -> Dict[str, Any]:
    return dict(
        Authorization=f"Bearer {access_token}"
    )
