from fastapi import APIRouter
from .schemes import RequestCreateOrder, RequestUpdateOrder
from .doc_info import doc_create_order, doc_get_order_by_id, doc_update_order, doc_delete_order

orders_router = APIRouter()


@orders_router.post('/orders', **doc_create_order)
def create_order(data: RequestCreateOrder):
    pass


@orders_router.get('/orders/{order_id}', **doc_get_order_by_id)
def get_order_by_id(order_id: str):
    pass


@orders_router.put('/orders/{order_id}', **doc_update_order)
def update_order(order_id: str, data: RequestUpdateOrder):
    pass


@orders_router.delete('/orders/{order_id}', **doc_delete_order)
def delete_order_by_id(order_id: str):
    pass
