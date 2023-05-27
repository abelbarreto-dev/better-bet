from typing import Any
from datetime import datetime
from decimal import Decimal


def get_decimal_str_or_none(value: Decimal) -> Any:
    if value is not None:
        return str(value)

    return value


def get_datetime_str_or_none(value: datetime) -> Any:
    if value is not None:
        return str(value)

    return value
