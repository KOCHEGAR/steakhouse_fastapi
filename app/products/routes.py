from fastapi import APIRouter, Depends, Body

# from app.helpers import Pag
from app.utils.pagination import Paginator
from . import functions as funcs
from .doc_info import doc_get_products, doc_update_product, doc_get_product, doc_create_product, doc_delete_product
from .schemes import RequestUpdateProduct, RequestCreateProduct

products_router = APIRouter()


@products_router.get('/products', **doc_get_products)
def get_products(pag: Paginator = Depends()):
    kwargs = {'paginator_instance': pag}
    return funcs.get_products(**kwargs)


@products_router.post('/products', **doc_create_product)
def create_product(data: RequestCreateProduct):
    kwargs = {'data': data.dict()}
    return funcs.create_product(**kwargs)


@products_router.get('/products/{product_id}', **doc_get_product)
def get_product(product_id: str):
    kwargs = {'id': product_id}
    return funcs.get_product(**kwargs)


@products_router.post('/products/{product_id}', **doc_update_product)
def update_product(product_id: str, data: RequestUpdateProduct):
    kwargs = {'id': product_id, 'data': data.dict(exclude_none=True, exclude_unset=True)}
    funcs.update_product(**kwargs)


@products_router.delete('/products/{product_id}', **doc_delete_product)
def delete_product(product_id):
    kwargs = {'id': product_id}
    funcs.delete_product(**kwargs)
