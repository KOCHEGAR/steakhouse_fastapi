from config import config
from fastapi import FastAPI

from .orders.routes import orders_router

app = FastAPI()


app.include_router(orders_router, prefix='/api', tags=['Orders operation'])
