from datetime import datetime
from src.utils.bet_status import BetStatus

from typing import Optional, List

from pydantic import BaseModel

from decimal import Decimal


class Login(BaseModel):
    player_name: str
    username: str
    password: str
    id: Optional[int] = None


class SingleBet(BaseModel):
    id_login: int
    odd: Decimal
    value_invest: Decimal
    description: Optional[str] = None
    home_team: Optional[str] = None
    away_team: Optional[str] = None
    team_bet: Optional[str] = None
    id: Optional[int] = None
    profit: Optional[Decimal] = None
    potential_earnings: Optional[Decimal] = None
    total_amount: Optional[Decimal] = None
    bet_status: Optional[BetStatus] = None
    create_datetime: Optional[datetime] = None
    finish_datetime: Optional[datetime] = None
    operator_fee: Optional[Decimal] = None


class MultiBet(BaseModel):
    id_login: int
    value_invest: Decimal
    description: Optional[str] = None
    home_team: Optional[str] = None
    away_team: Optional[str] = None
    team_bet: Optional[str] = None
    multi_odds: List[Decimal] = None
    id: Optional[int] = None
    profit: Optional[Decimal] = None
    potential_earnings: Optional[Decimal] = None
    total_amount: Optional[Decimal] = None
    bet_status: Optional[BetStatus] = None
    create_datetime: Optional[datetime] = None
    finish_datetime: Optional[datetime] = None
    operator_fee: Optional[Decimal] = None


class CompoundInterest(BaseModel):
    capital: Decimal
    interest_rate: Decimal
    time_opp: Decimal
    amount: Optional[Decimal] = None
