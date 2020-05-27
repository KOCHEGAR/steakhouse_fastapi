from fastapi import APIRouter, Depends

from . import functions as funcs
from .doc_info import doc_create_order, doc_get_order_by_id, doc_update_order, \
    doc_delete_order, doc_get_orders
from .schemes import RequestCreateOrder, RequestUpdateOrder
from app.utils.pagination import Paginator

orders_router = APIRouter()


@orders_router.get('/orders', **doc_get_orders)
def get_orders(pag: Paginator = Depends()):
    kwargs = {'paginator_instance': pag}
    return funcs.get_orders(**kwargs)


@orders_router.post('/orders', **doc_create_order)
def create_order(data: RequestCreateOrder):
    return funcs.create_order(**data.dict())


@orders_router.get('/orders/{order_id}', **doc_get_order_by_id)
def get_order_by_id(order_id: str):
    kwargs = {'id': order_id}
    return funcs.get_order(**kwargs)


@orders_router.put('/orders/{order_id}', **doc_update_order)
def update_order(order_id: str, data: RequestUpdateOrder):
    kwargs = {'id': order_id, 'data': data.dict(exclude_none=True, exclude_unset=True)}
    # funcs.update_order(**kwargs)
    # think about updating order


@orders_router.delete('/orders/{order_id}', **doc_delete_order)
def delete_order_by_id(order_id: str):
    kwargs = {'id': order_id}
    funcs.delete_order(**kwargs)
