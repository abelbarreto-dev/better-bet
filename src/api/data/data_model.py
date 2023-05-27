from peewee import (
    Model,
    AutoField,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKeyField,
    TextField
)

from src.utils.connection import Database


class BaseModel(Model):
    class Meta:
        database = Database.connect()


class Login(BaseModel):
    id = AutoField(null=False, primary_key=True)
    player_name = CharField(max_length=128, null=False)
    username = CharField(max_length=128, unique=True, null=False)
    password = CharField(max_length=512, null=False)


class SingleBet(BaseModel):
    id = AutoField(null=False, primary_key=True)
    id_login = ForeignKeyField(Login, Login.id, null=False)
    home_team = CharField(max_length=128, null=False)
    away_team = CharField(max_length=128, null=False)
    team_bet = CharField(max_length=128, null=True)
    odd = DecimalField(decimal_places=3, null=False)
    value_invest = DecimalField(decimal_places=2, null=False)
    profit = DecimalField(decimal_places=2, null=True)
    potential_earnings = DecimalField(decimal_places=2, null=True)
    total_amount = DecimalField(decimal_places=2, null=True)
    bet_status = CharField(max_length=64, null=True)
    description = CharField(max_length=256, null=True)
    create_datetime = DateTimeField(null=False)
    finish_datetime = DateTimeField(null=True)
    operator_fee = DecimalField(decimal_places=2, null=True)


class MultiBet(BaseModel):
    id = AutoField(null=False, primary_key=True)
    id_login = ForeignKeyField(Login, Login.id, null=False)
    home_team = CharField(max_length=128, null=False)
    away_team = CharField(max_length=128, null=False)
    team_bet = CharField(max_length=128, null=True)
    value_invest = DecimalField(decimal_places=2, null=False)
    multi_odds = TextField(null=True)
    profit = DecimalField(decimal_places=2, null=True)
    potential_earnings = DecimalField(decimal_places=2, null=True)
    total_amount = DecimalField(decimal_places=2, null=True)
    bet_status = CharField(max_length=64, null=True)
    description = CharField(max_length=256, null=True)
    create_datetime = DateTimeField(null=False)
    finish_datetime = DateTimeField(null=True)
    operator_fee = DecimalField(decimal_places=2, null=True)
