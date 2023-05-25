from src.utils.connection import Database

from src.api.data.data_model import (
    Login,
    SingleBet,
    MultiBet,
)


def create_login() -> None:
    with Database.connect() as db:
        db.create_tables([Login])


def create_single_bet() -> None:
    with Database.connect() as db:
        db.create_tables([SingleBet])


def create_multi_bet() -> None:
    with Database.connect() as db:
        db.create_tables([MultiBet])
