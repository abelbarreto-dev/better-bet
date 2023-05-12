from pydantic import BaseModel

from typing import Optional

from decimal import Decimal

from datetime import datetime

from src.utils.bet_status import BetStatus


class BetPatchBody(BaseModel):
    id: int
    bet_status: BetStatus
    finish_datetime: datetime
    operator_fee: Decimal
    total_amount: Decimal
    profit: Decimal
