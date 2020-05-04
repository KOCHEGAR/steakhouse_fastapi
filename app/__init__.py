from config import config
from fastapi import FastAPI

from .orders.routes import orders_router
from .cart.routes import cart_router
from .products.routes import products_router
from .types.routes import types_router
from .subtypes.routes import subtypes_router

app = FastAPI()


app.include_router(orders_router, prefix='/api', tags=['Orders operations'])
app.include_router(cart_router, prefix='/api', tags=['Cart operations'])
app.include_router(types_router, prefix='/api', tags=['Types operations'])
app.include_router(subtypes_router, prefix='/api', tags=['Subtypes operations'])
app.include_router(products_router, prefix='/api', tags=['Products operations'])
