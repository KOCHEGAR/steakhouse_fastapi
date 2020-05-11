from fastapi import APIRouter, Depends, Body
from .doc_info import doc_get_products, doc_update_product
from .schemes import RequestUpdateProduct
from . import functions as funcs
# from app.helpers import Pag
from app.utils.pagination import Paginator

products_router = APIRouter()


@products_router.get('/products', **doc_get_products)
def get_products(pag: Paginator = Depends()):
    kwargs = {'painator_instance': pag}
    return funcs.get_products(**kwargs)


@products_router.post('/products')
def create_product():
    pass


@products_router.get('/products/{product_id}')
def get_product(product_id: str):
    return funcs.get_product(product_id)


@products_router.post('/products/{product_id}', **doc_update_product)
def update_product(product_id: str, data: RequestUpdateProduct = Body(...)):
    print('data 1-> ', data.dict(exclude_unset=True, exclude_none=True))
    return funcs.update_product(product_id, data.dict(exclude_unset=True, exclude_none=True))
    pass


@products_router.delete('/products/{product_id}')
def delete_product(product_id):
    pass
