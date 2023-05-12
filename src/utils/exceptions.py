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


class ValueInvestException(ValueError):
    def __init__(self):
        super().__init__("error: value_invest is an invalid pattern")


class ProfitException(ValueError):
    def __init__(self):
        super().__init__("error: profit is in an invalid pattern")


class PotentialEarningsException(ValueError):
    def __init__(self):
        super().__init__("error: potential_earnings is in an invalid pattern")


class TotalAmountException(ValueError):
    def __init__(self):
        super().__init__("error: total_amount is in an invalid pattern")


class OperatorFeeException(ValueError):
    def __init__(self):
        super().__init__("error: operator_fee is in an invalid pattern")


class HomeTeamException(ValueError):
    def __init__(self):
        super().__init__("error: home_team is an invalid pattern")


class AwayTeamException(ValueError):
    def __init__(self):
        super().__init__("error: away_team is an invalid pattern")


class TeamBetException(ValueError):
    def __init__(self):
        super().__init__("error: team_bet is an invalid pattern")
