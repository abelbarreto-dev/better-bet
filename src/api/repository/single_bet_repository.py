from fastapi import Response

from starlette.responses import JSONResponse

from src.api.models.request_body import BetPatchBody
from src.api.models.api_models import SingleBet
from src.api.data.data_model import SingleBet as SingleBetDb

from src.utils.create_tables import create_single_bet
from src.utils.exceptions import (
    UnprocessedEntityException,
    DataNotFound,
    BadRequest,
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
