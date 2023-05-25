import datetime
from re import match

from decimal import Decimal

from src.api.models.api_models import (
    Login,
    LoginAuth,
    SingleBet,
    MultiBet,
    CompoundInterest
)

from src.api.models.request_body import (
    BetPatchBody,
    DateFromToBody,
)

from src.utils.exceptions import (
    PlayerNameException,
    UsernameException,
    PasswordException,
    DescriptionException,
    OddException,
    MoneyException,
    PercentException,
    TeamBetException,
    DatetimeNoneException,
    TimeOppException,
    DatetimeSmallException,
    DateToNoneException,
    DateFromGreaterException,
)


class Regex:
    username = r"^[_a-z]{1,64}$"
    password = r"^.{1,512}$"
    description = r"^.{1,256}$"
    player_name = r"^[a-zA-Z0-9\s]+$"
    team_bet = r"^.{1,128}$"
    money = r"^-?[0-9]{1,}\.[0-9]{2}$"
    percent = r"^-?[0-9]{1}\.[0-9]{1,5}$"
    odd = r"^[1-9]{1,}\.[0-9]{1,3}$"
    time_opp = r"^-?[0-9]{1,}\.?[0-9]{1,5}$"


def create_login_checker(login: Login) -> None:
    player_name_checker(login.player_name)
    username_checker(login.username)
    password_checker(login.password)


def login_auth_checker(login_auth: LoginAuth) -> None:
    username_checker(login_auth.username)
    password_checker(login_auth.password)


def single_bet_checker(single_bet: SingleBet) -> None:
    team_checker(single_bet.home_team, "home_team")
    team_checker(single_bet.away_team, "away_team")
    team_checker(single_bet.team_bet, "team_bet")
    odd_checker(single_bet.odd)
    money_checker(single_bet.value_invest, "value_invest")
    money_checker(single_bet.profit, "profit")
    money_checker(single_bet.potential_earnings, "potential_earnings")
    money_checker(single_bet.total_amount, "total_amount")
    percent_checker(single_bet.operator_fee, "operator_fee")
    description_checker(single_bet.description)
    datetime_small_than(
        single_bet.create_datetime,
        single_bet.finish_datetime,
        "create_datetime",
        "finish_datetime"
    )


def multi_bet_checker(multi_bet: MultiBet) -> None:
    team_checker(multi_bet.home_team, "home_team")
    team_checker(multi_bet.away_team, "away_team")
    team_checker(multi_bet.team_bet, "team_bet")

    for odd in multi_bet.multi_odds:
        odd_checker(odd)

    money_checker(multi_bet.value_invest, "value_invest")
    money_checker(multi_bet.profit, "profit")
    money_checker(multi_bet.potential_earnings, "potential_earnings")
    money_checker(multi_bet.total_amount, "total_amount")
    percent_checker(multi_bet.operator_fee, "operator_fee")
    description_checker(multi_bet.description)
    datetime_small_than(
        multi_bet.create_datetime,
        multi_bet.finish_datetime,
        "create_datetime",
        "finish_datetime"
    )


def single_bet_patch_checker(single_bet: BetPatchBody) -> None:
    percent_checker(single_bet.operator_fee, "operator_fee")
    money_checker(single_bet.total_amount, "total_amount")
    money_checker(single_bet.profit, "profit")
    datetime_none_checker(single_bet.finish_datetime, "finish_datetime")


def multi_bet_patch_checker(multi_bet: BetPatchBody) -> None:
    percent_checker(multi_bet.operator_fee, "operator_fee")
    money_checker(multi_bet.total_amount, "total_amount")
    money_checker(multi_bet.profit, "profit")
    datetime_none_checker(multi_bet.finish_datetime, "finish_datetime")


def compound_interest_checker(compound_interest: CompoundInterest) -> None:
    money_checker(compound_interest.capital, "capital")
    percent_checker(compound_interest.interest_rate, "interest_rate")
    money_checker(compound_interest.amount, "amount")
    time_opp_checker(compound_interest.time_opp)


def date_from_to_checker(date_from_to: DateFromToBody, is_multi: bool) -> None:
    what_bet = "multi bet" if is_multi else "single bet"

    if date_from_to.date_to is None:
        raise DateToNoneException(what_bet)

    if date_from_to.date_from > date_from_to.date_to:
        raise DateFromGreaterException(what_bet)


def time_opp_checker(time_opp: Decimal) -> None:
    if time_opp is not None and not match(Regex.time_opp, str(time_opp)):
        raise TimeOppException()


def team_checker(team: str, what_team: str) -> None:
    if team is not None and not match(Regex.team_bet, team):
        raise TeamBetException(what_team)


def player_name_checker(player_name: str) -> None:
    if not match(Regex.player_name, player_name):
        raise PlayerNameException()


def username_checker(username: str) -> None:
    if not match(Regex.username, username):
        raise UsernameException()


def password_checker(password: str) -> None:
    if not match(Regex.password, password):
        raise PasswordException()


def description_checker(description: str) -> None:
    if description is not None and not match(Regex.description, description):
        raise DescriptionException()


def money_checker(money: Decimal, what_money: str) -> None:
    if money is not None and not match(Regex.money, str(money)):
        raise MoneyException(what_money)


def percent_checker(percent: Decimal, what_percent: str) -> None:
    if percent is not None and not match(Regex.percent, str(percent)):
        raise PercentException(what_percent)


def odd_checker(odd: Decimal) -> None:
    if not match(Regex.odd, str(odd)):
        raise OddException()


def datetime_none_checker(datetime_test: datetime.datetime, what_dtt: str) -> None:
    if datetime_test is None:
        raise DatetimeNoneException(what_dtt)


def datetime_small_than(
    datetime_1: datetime.datetime,
    datetime_2: datetime.datetime,
    what_dtt_1: str,
    what_dtt_2: str
) -> None:
    if datetime_2 is not None and datetime_1 > datetime_2:
        raise DatetimeSmallException(what_dtt_1, what_dtt_2)
