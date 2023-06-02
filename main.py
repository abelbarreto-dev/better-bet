import subprocess

from fastapi import FastAPI

from src.api.controller.controller import ROUTER


app = FastAPI()
app.include_router(ROUTER)
