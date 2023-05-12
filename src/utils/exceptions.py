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
