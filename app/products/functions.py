
from .models import Product
from .schemes import ResponseGetProducts
from app.utils.mongoengine_helpers import get_model_by_id_or_raise
from app.utils.errors import SteakhouseException


def create_dummy_products():
    from random import randint
    from uuid import uuid4

    for i in range(2000):
        p = Product()
        p.title = f'item_{str(uuid4())}_{i}'
        p.barcode = str(randint(200000, 3000000))
        p.product_code = str(randint(400000, 500000))
        p.price = float(randint(20, 300))
        p.weight = randint(50, 1000)
        p.save()


def get_products(*args, **kwargs):
    return kwargs['paginator_instance'].paginate_model(ResponseGetProducts, Product)


def get_product(*args, **kwargs):
    item_id = kwargs['id']
    return get_model_by_id_or_raise(Product, item_id)


def create_product(*args, **kwargs):
    data = kwargs['data']


def update_product(*args, **kwargs):
    item_id = kwargs['id']
    data = kwargs['data']

    if not data:
        raise SteakhouseException(f'Empty data to update')

    product = get_model_by_id_or_raise(Product, item_id)
    product.update(**data)


def delete_product(*args, **kwargs):
    item_id = kwargs['id']
    product = get_model_by_id_or_raise(Product, item_id)
    product.delete()
