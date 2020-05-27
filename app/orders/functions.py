from .models import Order
from app.utils.mongoengine_helpers import get_model_by_id_or_raise
from .schemes import ResponseGetOrders
from app.utils.logging import logging_decorator


@logging_decorator('orders.log', 'orders_logger', 'CREATE ORDER')
def create_order(*args, **kwargs):
    print(args, kwargs)


@logging_decorator('orders.log', 'orders_logger', 'GET ORDER')
def get_order(*args, **kwargs):
    item_id = kwargs['id']
    return get_model_by_id_or_raise(Order, item_id)


@logging_decorator('orders.log', 'orders_logger', 'GET ORDERS')
def get_orders(*args, **kwargs):
    return kwargs['paginator_instance'].paginate_model(ResponseGetOrders, Order)


@logging_decorator('orders.log', 'orders_logger', 'UPDATE ORDER')
def update_order(*args, **kwargs):
    pass


@logging_decorator('orders.log', 'orders_logger', 'DELETE ORDER')
def delete_order(*args, **kwargs):
    pass
