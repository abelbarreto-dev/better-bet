from fastapi import Response

from starlette.responses import JSONResponse

from src.api.models.request_body import BetPatchBody
from src.api.models.api_models import MultiBet
from src.api.data.data_model import MultiBet as MultiBetDb

from src.utils.create_tables import create_multi_bet
from src.utils.exceptions import (
    UnprocessedEntityException,
    DataNotFound,
    BadRequest,
)


class MultiBetRepository:
    @classmethod
    async def _multi_bet_table(cls) -> None:
        create_multi_bet()

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
            bet_multi: MultiBetDb = MultiBetDb.get(
                MultiBetDb.id == multi_bet.id
            )

            bet_multi.bet_status = multi_bet.bet_status
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
