from datetime import datetime
from enum import Enum

from typing import Optional, List

from pydantic import BaseModel

from decimal import Decimal


class Login(BaseModel):
    player_name: str
    username: str
    password: str
    id: Optional[int] = None


class BetStatus(Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'


class SingleBet(BaseModel):
    id_login: int
    home_team: str
    away_team: str
    team_bet: str
    odd: Decimal
    value_invest: Decimal
    id: Optional[int] = None
    profit: Optional[Decimal] = None
    bet_status: Optional[BetStatus] = None
    description: Optional[str] = None
    create_datetime: Optional[datetime] = None
    finish_datetime: Optional[datetime] = None


class MultiBet(BaseModel):
    id_login: int
    home_team: str
    away_team: str
    team_bet: str
    value_invest: Decimal
    multi_odds: List[Decimal] = None
    id: Optional[int] = None
    profit: Optional[Decimal] = None
    bet_status: Optional[BetStatus] = None
    description: Optional[str] = None
    create_datetime: Optional[datetime] = None
    finish_datetime: Optional[datetime] = None
