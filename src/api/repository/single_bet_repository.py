from fastapi import Response

from starlette.responses import JSONResponse

from src.api.models.request_body import DateFilterBody
from src.api.models.request_body import BetPatchBody
from src.api.models.api_models import SingleBet
from src.api.data.data_model import SingleBet as SingleBetDb
from src.utils.bet_status import BetStatus

from src.utils.create_tables import create_single_bet
from src.utils.exceptions import (
    UnprocessedEntityException,
    DataNotFound,
)


class SingleBetRepository:
    @classmethod
    async def _single_bet_table(cls) -> None:
        create_single_bet()

    @classmethod
    async def create_single_bet(cls, single_bet: SingleBet) -> Response:
        await cls._single_bet_table()

        try:
            new_single_bet = SingleBetDb.insert(**single_bet.dict())

            new_single_bet.execute()
        except Exception:
            raise UnprocessedEntityException("SingleBet")

        return Response(
            status_code=204,
        )

    @classmethod
    async def patch_single_bet(cls, single_bet: BetPatchBody) -> Response:
        await cls._single_bet_table()

        try:
            bet_single: SingleBetDb = SingleBetDb.get(
                SingleBetDb.id == single_bet.id
            )

            bet_single.bet_status = single_bet.bet_status
            bet_single.finish_datetime = single_bet.finish_datetime
            bet_single.operator_fee = single_bet.operator_fee
            bet_single.total_amount = single_bet.total_amount
            bet_single.profit = single_bet.profit

            bet_single.save()
        except Exception:
            raise UnprocessedEntityException("SingleBet")

        return Response(
            status_code=204,
        )

    @classmethod
    async def get_single_bet_profits(cls, single_bet: DateFilterBody) -> JSONResponse:
        await cls._single_bet_table()

        try:
            bets_single: [SingleBetDb] = SingleBetDb.get(
                (SingleBetDb.id_login == single_bet.login_id) &
                (SingleBetDb.create_datetime == single_bet.date_from) &
                (SingleBetDb.finish_datetime == single_bet.date_to) &
                (SingleBetDb.bet_status == BetStatus.SUCCESS)
            )
        except Exception:
            raise DataNotFound("SingleBet profitable Not Found")

        return JSONResponse(
            content=dict(
                single_bet_profits=[
                    SingleBet(
                        id=single_bet.id,
                        id_login=single_bet.id_login,
                        home_team=single_bet.home_team,
                        away_team=single_bet.away_team,
                        team_bet=single_bet.team_bet,
                        odd=single_bet.odd,
                        value_invest=single_bet.value_invest,
                        profit=single_bet.profit,
                        potential_earnings=single_bet.potential_earnings,
                        total_amount=single_bet.total_amount,
                        bet_status=single_bet.bet_status,
                        description=single_bet.description,
                        create_datetime=single_bet.create_datetime,
                        finish_datetime=single_bet.finish_datetime,
                        operator_fee=single_bet.operator_fee,
                    )
                    for single_bet in bets_single
                ]
            )
        )

    @classmethod
    async def get_single_bet_lost(cls, single_bet: DateFilterBody) -> JSONResponse:
        await cls._single_bet_table()

        try:
            bets_single: [SingleBetDb] = SingleBetDb.get(
                (SingleBetDb.id_login == single_bet.login_id) &
                (SingleBetDb.create_datetime == single_bet.date_from) &
                (SingleBetDb.finish_datetime == single_bet.date_to) &
                (SingleBetDb.bet_status == BetStatus.FAILURE)
            )
        except Exception:
            raise DataNotFound("SingleBet lost Not Found")

        return JSONResponse(
            content=dict(
                single_bet_lost=[
                    SingleBet(
                        id=single_bet.id,
                        id_login=single_bet.id_login,
                        home_team=single_bet.home_team,
                        away_team=single_bet.away_team,
                        team_bet=single_bet.team_bet,
                        odd=single_bet.odd,
                        value_invest=single_bet.value_invest,
                        profit=single_bet.profit,
                        potential_earnings=single_bet.potential_earnings,
                        total_amount=single_bet.total_amount,
                        bet_status=single_bet.bet_status,
                        description=single_bet.description,
                        create_datetime=single_bet.create_datetime,
                        finish_datetime=single_bet.finish_datetime,
                        operator_fee=single_bet.operator_fee,
                    )
                    for single_bet in bets_single
                ]
            )
        )
