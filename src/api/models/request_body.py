from pydantic import BaseModel

from typing import Optional

from decimal import Decimal

from datetime import datetime, date

from src.utils.bet_status import BetStatus


class BetPatchBody(BaseModel):
    id: int
    bet_status: BetStatus
    finish_datetime: datetime
    operator_fee: Decimal
    total_amount: Decimal
    profit: Decimal


class DateFromToBody(BaseModel):
    login_id: int
    date_from: date
    date_to: Optional[date] = None


class DateFilterBody(BaseModel):
    login_id: int
    date_from: Optional[date] = None
    date_to: Optional[date] = None
