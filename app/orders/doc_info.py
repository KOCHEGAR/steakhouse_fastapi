from typing import List
from starlette.status import HTTP_201_CREATED
from app.helpers import DocInfo
from .schemes import ResponseCreateOrder, ResponseGetOrder


doc_get_orders = DocInfo(
    descr='Get list of orders',
    summ='Get orders',
    res_descr='List of orders',
    # resp_model=List[ResponseGetOrder]
).__dict__

doc_create_order = DocInfo(
    descr='Order creation. Example of ime format for order_time: ',
    summ='Create order',
    res_descr='Order created successfully',
    status_code=HTTP_201_CREATED,
    resp_model=ResponseCreateOrder
).__dict__


doc_get_order_by_id = DocInfo(
    descr='Get order by ID',
    summ='Get order by ID',
    res_descr='Retrieved order',
    resp_model=ResponseGetOrder
).__dict__


allowed_fields_to_update = [
    'on_site', 'order_status'
]

doc_update_order = DocInfo(
    descr=f'Update order by ID. Allowed fields to update: {allowed_fields_to_update}',
    summ='Update order',
    res_descr='Order updated'
).__dict__


doc_delete_order = DocInfo(
    descr='Delete order by ID',
    summ='Delete order',
    res_descr='Order deleted'
).__dict__
