from typing import Dict, Any

from fastapi import Response

from starlette.responses import JSONResponse

from src.api.models.request_body import (
    BetPatchBody,
    DateFilterBody,
    DateFromToBody,
)

from src.api.models.api_models import MultiBet
from src.api.data.data_model import MultiBet as MultiBetDb
from src.utils.bet_status import BetStatus

from src.utils.types_utils import (
    get_decimal_str_or_none,
    get_datetime_str_or_none,
)

from src.utils.create_tables import create_multi_bet
from src.utils.exceptions import (
    UnprocessedEntityException,
    DataNotFound,
)


class MultiBetRepository:
    @classmethod
    async def _multi_bet_table(cls) -> None:
        create_multi_bet()

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
    async def create_multi_bet(cls, multi_bet: MultiBet) -> Response:
        await cls._multi_bet_table()

        try:
            new_multi_bet = MultiBetDb.insert(**multi_bet.dict())

            new_multi_bet.execute()
        except Exception:
            raise UnprocessedEntityException("MultiBet")

        return Response(
            status_code=204,
        )

    @classmethod
    async def patch_multi_bet(cls, multi_bet: BetPatchBody) -> Response:
        await cls._multi_bet_table()

        try:
            bet_multi = MultiBetDb.get(
                MultiBetDb.id == multi_bet.id
            )

            bet_multi.bet_status = multi_bet.bet_status.value
            bet_multi.finish_datetime = multi_bet.finish_datetime
            bet_multi.operator_fee = multi_bet.operator_fee
            bet_multi.total_amount = multi_bet.total_amount
            bet_multi.profit = multi_bet.profit

            bet_multi.save()
        except Exception:
            raise UnprocessedEntityException("MultiBet")

        return Response(
            status_code=204,
        )

    @classmethod
    async def get_multi_bet_profits(cls, multi_bet: DateFilterBody) -> JSONResponse:
        await cls._multi_bet_table()

        try:
            bets_multi = MultiBetDb.select().where(
                (
                    MultiBetDb.id_login == multi_bet.login_id &
                    MultiBetDb.bet_status == BetStatus.SUCCESS.value
                ) &
                (
                    (MultiBetDb.create_datetime == multi_bet.date_from) |
                    (MultiBetDb.finish_datetime == multi_bet.date_to) |
                    (
                        MultiBetDb.create_datetime.is_null(False) &
                        MultiBetDb.create_datetime.cast("date") == multi_bet.date_from
                    ) |
                    (
                        MultiBetDb.finish_datetime.is_null(False) &
                        MultiBetDb.finish_datetime.cast("date") == multi_bet.date_to
                    )
                )
            )

            bets_list = list(bets_multi.dicts())
        except Exception:
            raise DataNotFound("MultiBet profitable Not Found")

        bets_list = [await cls._get_multi_bet(bet) for bet in bets_list]

        return JSONResponse(
            content=dict(
                multi_bet_profits=bets_list
            )
        )

    @classmethod
    async def get_multi_bet_lost(cls, multi_bet: DateFilterBody) -> JSONResponse:
        await cls._multi_bet_table()

        try:
            bets_multi = MultiBetDb.select().where(
                (
                    MultiBetDb.id_login == multi_bet.login_id &
                    MultiBetDb.bet_status == BetStatus.SUCCESS.value
                ) &
                (
                    (MultiBetDb.create_datetime == multi_bet.date_from) |
                    (MultiBetDb.finish_datetime == multi_bet.date_to) |
                    (
                        MultiBetDb.create_datetime.is_null(False) &
                        MultiBetDb.create_datetime.cast("date") == multi_bet.date_from
                    ) |
                    (
                        MultiBetDb.finish_datetime.is_null(False) &
                        MultiBetDb.finish_datetime.cast("date") == multi_bet.date_to
                    )
                )
            )

            bets_list = list(bets_multi.dicts())
        except Exception:
            raise DataNotFound("MultiBet lost Not Found")

        bets_list = [await cls._get_multi_bet(bet) for bet in bets_list]

        return JSONResponse(
            content=dict(
                multi_bet_lost=bets_list
            )
        )

    @classmethod
    async def get_multi_bet_filter(cls, multi_bet: DateFromToBody) -> JSONResponse:
        await cls._multi_bet_table()

        try:
            bets_multi = MultiBetDb.select().where(
                (MultiBetDb.id_login == multi_bet.login_id) &
                (
                    (MultiBetDb.create_datetime.cast("date") == multi_bet.date_from) |
                    (
                        (MultiBetDb.finish_datetime.is_null(False)) &
                        (MultiBetDb.finish_datetime.cast("date") == multi_bet.date_to)
                    )
                )
            )

            bets_list = list(bets_multi.dicts())
        except Exception:
            raise DataNotFound("MultiBet Not Found")

        bets_list = [await cls._get_multi_bet(bet) for bet in bets_list]

        return JSONResponse(
            content=dict(
                multi_bets=bets_list
            )
        )
