from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from mongoengine import connect, disconnect
from pymongo.errors import ServerSelectionTimeoutError
from starlette.exceptions import HTTPException

from config import config
from .cart.routes import cart_router
from .orders.routes import orders_router
from .products.routes import products_router
from .subtypes.routes import subtypes_router
from .types.routes import types_router
from .utils.errors import http_error_handler, handle_422, SteakhouseException, handle_db_connection_error

app = FastAPI()

app.include_router(orders_router, prefix='/api', tags=['Orders operations'])
# app.include_router(cart_router, prefix='/api', tags=['Cart operations'])
app.include_router(types_router, prefix='/api', tags=['Types operations'])
app.include_router(subtypes_router, prefix='/api', tags=['Subtypes operations'])
app.include_router(products_router, prefix='/api', tags=['Products operations'])

connect(
    username=config['MONGO_USER'],
    password=config['MONGO_PASSWORD'],
    host=config['MONGO_HOST'],
    port=config['MONGO_PORT'],
    db=config['MONGO_DBNAME']
)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(ServerSelectionTimeoutError, handle_db_connection_error)
app.add_exception_handler(SteakhouseException, http_error_handler)
app.add_exception_handler(RequestValidationError, handle_422)


@app.on_event('startup')
def startup():
    pass


@app.on_event('shutdown')
def shutdown():
    disconnect()
