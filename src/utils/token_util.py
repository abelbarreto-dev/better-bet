from os import getenv

from dotenv import load_dotenv

from typing import Dict, Any

from datetime import datetime, timedelta

from jose import jwt

from src.utils.types_utils import Token


def create_access_token(data: Dict[str, Any]) -> Token:
    load_dotenv()

    new_data = data.copy()

    secret_key = getenv("SECRET_KEY")
    expires_minutes = int(getenv("EXPIRES"))
    algorithm = getenv("ALGORITHM")

    expires = datetime.utcnow() + timedelta(expires_minutes)

    new_data.update({"exp": expires})

    token_jwt = jwt.encode(new_data, secret_key, algorithm=algorithm)

    return Token(token_jwt)


def check_access_token(token: Token) -> str:
    load_dotenv()

    secret_key = getenv("SECRET_KEY")
    algorithm = getenv("ALGORITHM")

    payload = jwt.decode(token, secret_key, algorithms=[algorithm])

    return payload.get("sub")
