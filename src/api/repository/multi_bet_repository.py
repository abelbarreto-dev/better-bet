from fastapi import Response

from starlette.responses import JSONResponse

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
