from fastapi import APIRouter, Depends
from .doc_info import doc_get_products
from . import functions as funcs
from app.helpers import Pag
products_router = APIRouter()


@products_router.get('/products', **doc_get_products)
def get_products(pag: Pag = Depends()):
    return funcs.get_products(**pag.dict())


@products_router.post('/products')
def create_product():
    pass


@products_router.get('/products/{product_id}')
def get_product(product_id):
    return funcs.get_product(product_id)


@products_router.put('/products/{product_id}')
def update_product(product_id):
    pass


@products_router.delete('/products/{product_id}')
def delete_product(product_id):
    pass
