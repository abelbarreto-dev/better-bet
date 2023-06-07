from typing import Any

from datetime import (
    datetime,
    timedelta,
)

from decimal import Decimal


class Token(str):
    pass


def get_decimal_str_or_none(value: Decimal) -> Any:
    if value is not None:
        return str(value)

    return value


def get_datetime_str_or_none(value: datetime) -> Any:
    if value is not None:
        return str(value)

    return value


def get_datetime_brazil() -> datetime:
    zone_brazil = timedelta(hours=-3)

    return datetime.utcnow() + zone_brazil
