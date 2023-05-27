from typing import Dict, Any

from starlette.responses import JSONResponse

from src.utils.bet_status import BetStatus

from src.api.data.data_model import (
    SingleBet as SingleBetDb,
    MultiBet as MultiBetDb,
)

from src.api.models.api_models import (
    SingleBet,
    MultiBet
)

from src.utils.create_tables import (
    create_multi_bet,
    create_single_bet,
)


class GetAllRepository:
    @classmethod
    async def _create_single_multi_table(cls) -> None:
        create_single_bet()
        create_multi_bet()

    @classmethod
    async def _get_single_bet(cls, single_bet: SingleBetDb) -> Dict[str, Any]:
        return dict(
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

    @classmethod
    async def _get_multi_bet(cls, multi_bet: MultiBetDb) -> Dict[str, Any]:
        return dict(
            id=multi_bet.id,
            id_login=multi_bet.id_login,
            home_team=multi_bet.home_team,
            away_team=multi_bet.away_team,
            team_bet=multi_bet.team_bet,
            value_invest=multi_bet.value_invest,
            multi_odds=multi_bet.multi_odds,
            profit=multi_bet.profit,
            potential_earnings=multi_bet.potential_earnings,
            total_amount=multi_bet.total_amount,
            bet_status=multi_bet.bet_status,
            description=multi_bet.description,
            create_datetime=multi_bet.create_datetime,
            finish_datetime=multi_bet.finish_datetime,
            operator_fee=multi_bet.operator_fee,
        )

    @classmethod
    async def get_all_profits_id_login(cls, id_login: int) -> JSONResponse:
        await cls._create_single_multi_table()

        bets_single: [SingleBetDb] = SingleBetDb.get(
            (SingleBetDb.id_login == id_login) &
            (SingleBetDb.bet_status == BetStatus.SUCCESS)
        )

        bets_multi: [MultiBetDb] = MultiBetDb.get(
            (MultiBetDb.id_login == id_login) &
            (MultiBetDb.bet_status == BetStatus.SUCCESS)
        )

        return JSONResponse(
            content=dict(
                single_bets_profits=[
                    await cls._get_single_bet(single_bet)
                    for single_bet in bets_single
                ],
                multi_bets_profits=[
                    await cls._get_multi_bet(multi_bet)
                    for multi_bet in bets_multi
                ]
            )
        )

    @classmethod
    async def get_all_lost_id_login(cls, id_login: int) -> JSONResponse:
        await cls._create_single_multi_table()

        try:
            bets_single: [SingleBetDb] = SingleBetDb.get(
                (SingleBetDb.id_login == id_login) &
                (SingleBetDb.bet_status == BetStatus.FAILURE)
            )
        except Exception:
            bets_single = []

        try:
            bets_multi: [MultiBetDb] = MultiBetDb.get(
                (MultiBetDb.id_login == id_login) &
                (MultiBetDb.bet_status == BetStatus.FAILURE)
            )
        except Exception:
            bets_multi = []

        return JSONResponse(
            content=dict(
                single_bets_lost=[
                    await cls._get_single_bet(single_bet)
                    for single_bet in bets_single
                ],
                multi_bets_lost=[
                    await cls._get_multi_bet(multi_bet)
                    for multi_bet in bets_multi
                ]
            )
        )
