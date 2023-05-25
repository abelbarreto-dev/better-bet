from fastapi import HTTPException


class PlayerNameException(ValueError):
    def __init__(self):
        super().__init__("error: player_name is an invalid pattern")


class UsernameException(ValueError):
    def __init__(self):
        super().__init__("error: username is an invalid pattern")


class PasswordException(ValueError):
    def __init__(self):
        super().__init__("error: password is an invalid pattern")


class DescriptionException(ValueError):
    def __init__(self):
        super().__init__("error: description is an invalid pattern")


class OddException(ValueError):
    def __init__(self):
        super().__init__("error: odd value is an invalid pattern")


class MoneyException(ValueError):
    def __init__(self, what_money: str):
        super().__init__(f"error: {what_money} is an invalid pattern")


class PercentException(ValueError):
    def __init__(self, what_percent: str):
        super().__init__(f"error: {what_percent} is in an invalid pattern")


class TeamBetException(ValueError):
    def __init__(self, what_team: str):
        super().__init__(f"error: {what_team} is an invalid pattern")


class DatetimeSmallException(ValueError):
    def __init__(self, what_dtt_1: str, what_dtt_2: str):
        super().__init__(f"error: {what_dtt_1} can't be greater than {what_dtt_2}")


class DatetimeNoneException(ValueError):
    def __init__(self, what_dtt: str):
        super().__init__(f"error: {what_dtt} can't be null")


class TimeOppException(ValueError):
    def __init__(self):
        super().__init__("error: time_opp is an invalid pattern")


class DateToNoneException(ValueError):
    def __init__(self, what_bet: str):
        super().__init__(f"error: date_to can not be null at {what_bet}")


class DateFromGreaterException(ValueError):
    def __init__(self, what_bet: str):
        super().__init__(f"error: date_from can not be greater than date_to at {what_bet}")


class BadRequest(HTTPException):
    def __init__(self, message: str):
        super().__init__(
            status_code=400,
            detail={"message": message}
        )


class DataNotFound(HTTPException):
    def __init__(self, message: str):
        super().__init__(
            status_code=404,
            detail={"message": f"error: {message}"}
        )
