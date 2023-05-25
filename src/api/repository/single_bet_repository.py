from fastapi import Response

from starlette.responses import JSONResponse

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
