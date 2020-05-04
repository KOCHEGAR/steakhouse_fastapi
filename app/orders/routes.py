from fastapi import APIRouter, Depends
from . import functions as funcs
from .schemes import RequestCreateOrder, RequestUpdateOrder
from .doc_info import doc_create_order, doc_get_order_by_id, doc_update_order, \
    doc_delete_order, doc_get_orders


orders_router = APIRouter()

# from fastapi import Query
# from pydantic import BaseModel
#
#
# class Pag(BaseModel):
#     # sort:
#     limit: int = Query(200, title='Limit!')
#     offset: int = Query(1, title='Offset!')
#     select_fields: str = Query('', title='Comma-separated list of fields to retrieve')


@orders_router.get('/orders', **doc_get_orders)
def get_orders():
    pass


@orders_router.post('/orders', **doc_create_order)
def create_order(data: RequestCreateOrder):
    return funcs.create_order(**data.dict())


@orders_router.get('/orders/{order_id}', **doc_get_order_by_id)
def get_order_by_id(order_id: str):
    pass


@orders_router.put('/orders/{order_id}', **doc_update_order)
def update_order(order_id: str, data: RequestUpdateOrder):
    pass


@orders_router.delete('/orders/{order_id}', **doc_delete_order)
def delete_order_by_id(order_id: str):
    pass
