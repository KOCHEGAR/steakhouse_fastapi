from typing import List

from fastapi import FastAPI
from fastapi_contrib.db.utils import setup_mongodb
from fastapi_contrib.conf import settings


# from .helpers import http_error_handler, http_422_error_handler
from .orders.routes import orders_router


app = FastAPI()
settings.mongodb_max_pool_size = 20
settings.mongodb_dbname = 'steakhouse'
settings.mongodb_dsn = 'mongodb://127.0.0.1:27017'
settings.fastapi_app = 'app.app'


app.include_router(orders_router, prefix='/api', tags=['Orders'])



# app.add_exception_handler(HTTPException, http_error_handler)
# app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

@app.on_event('startup')
async def startup():
    setup_mongodb(app)
