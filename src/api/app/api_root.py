from fastapi import FastAPI

from src.api.resource.api_resource import ROUTER


better_bet_api = FastAPI()

better_bet_api.include_router(ROUTER)
