from typing import Dict, Any

from starlette.responses import JSONResponse

from src.utils.bet_status import BetStatus

from src.api.data.data_model import (
    SingleBet as SingleBetDb,
    MultiBet as MultiBetDb,
)

from src.utils.create_tables import (
    create_multi_bet,
    create_single_bet,
)

from src.utils.types_utils import (
    get_decimal_str_or_none,
    get_datetime_str_or_none,
)

from src.utils.exceptions import DataNotFound


class GetAllRepository:
    @classmethod
    async def _create_single_multi_table(cls) -> None:
        create_single_bet()
        create_multi_bet()

    @classmethod
    async def _get_single_bet(cls, single_bet: Dict[str, Any]) -> Dict[str, Any]:
        datetime_create = get_datetime_str_or_none(single_bet["create_datetime"])
        datetime_finish = get_datetime_str_or_none(single_bet["finish_datetime"])

        return {
            "id": single_bet["id"],
            "id_login": single_bet["id_login"],
            "home_team": single_bet["home_team"],
            "away_team": single_bet["away_team"],
            "team_bet": single_bet["team_bet"],
            "odd": get_decimal_str_or_none(single_bet["odd"]),
            "value_invest": get_decimal_str_or_none(single_bet["value_invest"]),
            "profit": get_decimal_str_or_none(single_bet["profit"]),
            "potential_earnings": get_decimal_str_or_none(single_bet["potential_earnings"]),
            "total_amount": get_decimal_str_or_none(single_bet["total_amount"]),
            "bet_status": single_bet["bet_status"],
            "description": single_bet["description"],
            "create_datetime": datetime_create,
            "finish_datetime": datetime_finish,
            "operator_fee": get_decimal_str_or_none(single_bet["operator_fee"]),
        }

    @classmethod
    async def _get_multi_bet(cls, multi_bet: MultiBetDb) -> Dict[str, Any]:
        datetime_create = get_datetime_str_or_none(multi_bet.create_datetime)
        datetime_finish = get_datetime_str_or_none(multi_bet.finish_datetime)

        return {
            "id": multi_bet["id"],
            "id_login": multi_bet["id_login"],
            "home_team": multi_bet["home_team"],
            "away_team": multi_bet["away_team"],
            "team_bet": multi_bet["team_bet"],
            "value_invest": get_decimal_str_or_none(multi_bet["value_invest"]),
            "multi_odds": [
                get_decimal_str_or_none(odd)
                for odd in multi_bet["multi_odds"]
            ],
            "profit": get_decimal_str_or_none(multi_bet["profit"]),
            "potential_earnings": get_decimal_str_or_none(multi_bet["potential_earnings"]),
            "total_amount": get_decimal_str_or_none(multi_bet["total_amount"]),
            "bet_status": multi_bet["bet_status"],
            "description": multi_bet["description"],
            "create_datetime": datetime_create,
            "finish_datetime": datetime_finish,
            "operator_fee": get_decimal_str_or_none(multi_bet["operator_fee"]),
        }

    @classmethod
    async def get_all_profits_id_login(cls, id_login: int) -> JSONResponse:
        await cls._create_single_multi_table()

        bets_single = SingleBetDb.select().where(
            (SingleBetDb.id_login == id_login) &
            (SingleBetDb.bet_status == BetStatus.SUCCESS.value)
        )

        bets_multi = MultiBetDb.select().where(
            (MultiBetDb.id_login == id_login) &
            (MultiBetDb.bet_status == BetStatus.SUCCESS.value)
        )

        single_list = list(bets_single.dicts())
        multi_list = list(bets_multi.dicts())

        if not single_list and not multi_list:
            raise DataNotFound("any bets not found")

        single_list = [await cls._get_single_bet(bet) for bet in single_list]
        multi_list = [await cls._get_multi_bet(bet) for bet in multi_list]

        return JSONResponse(
            content=dict(
                single_bets_profits=single_list,
                multi_bets_profits=multi_list,
            )
        )

    @classmethod
    async def get_all_lost_id_login(cls, id_login: int) -> JSONResponse:
        await cls._create_single_multi_table()

        bets_single = SingleBetDb.select().where(
            (SingleBetDb.id_login == id_login) &
            (SingleBetDb.bet_status == BetStatus.FAILURE.value)
        )

        bets_multi = MultiBetDb.select().where(
            (MultiBetDb.id_login == id_login) &
            (MultiBetDb.bet_status == BetStatus.FAILURE.value)
        )

        single_list = list(bets_single.dicts())
        multi_list = list(bets_multi.dicts())

        if not single_list and not multi_list:
            raise DataNotFound("any bets not found")

        single_list = [await cls._get_single_bet(bet) for bet in single_list]
        multi_list = [await cls._get_multi_bet(bet) for bet in multi_list]

        return JSONResponse(
            content=dict(
                single_bets_lost=single_list,
                multi_bets_lost=multi_list,
            )
        )
