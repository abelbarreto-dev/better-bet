from fastapi import FastAPI

import uvicorn

from src.api.resource.api_resource import ROUTER


better_bet_api = FastAPI()

if __name__ == '__main__':
    better_bet_api.include_router(ROUTER)

    uvicorn.run(better_bet_api)
