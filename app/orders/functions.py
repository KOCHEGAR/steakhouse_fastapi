from .models import Order
from app.utils.mongoengine_helpers import get_model_by_id_or_raise
from .schemes import ResponseGetOrders


def create_order(*args, **kwargs):
    print(args, kwargs)


def get_order(*args, **kwargs):
    item_id = kwargs['id']
    return get_model_by_id_or_raise(Order, item_id)


def get_orders(*args, **kwargs):
    return kwargs['paginator_instance'].paginate_model(ResponseGetOrders, Order)


def update_order(*args, **kwargs):
    pass


def delete_order(*args, **kwargs):
    pass
