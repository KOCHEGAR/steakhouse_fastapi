
from .models import Product
from .schemes import ResponseGetProducts
from app.utils.mongoengine_helpers import get_model_by_id_or_raise
from app.utils.errors import SteakhouseException
from app.utils.logging import logging_decorator


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


@logging_decorator('products.log', 'products_logger', 'GET PRODUCTS')
def get_products(*args, **kwargs):
    return kwargs['paginator_instance'].paginate_model(ResponseGetProducts, Product)


@logging_decorator('products.log', 'products_logger', 'GET PRODUCT')
def get_product(*args, **kwargs):
    item_id = kwargs['id']
    return get_model_by_id_or_raise(Product, item_id)


@logging_decorator('products.log', 'products_logger', 'CREATE PRODUCT')
def create_product(*args, **kwargs):
    data = kwargs['data']
    return Product(**data).save()


# @logging_decorator('products.log', 'products_logger', 'ADD IMAGE')
# def add_image_to_product(*args, **kwargs):
#   image will be generated in saved here...
#
#   will be implemented later...
#   pass


@logging_decorator('products.log', 'products_logger', 'UPDATE PRODUCT')
def update_product(*args, **kwargs):
    item_id = kwargs['id']
    data = kwargs['data']

    if not data:
        raise SteakhouseException(f'Empty data to update')

    product = get_model_by_id_or_raise(Product, item_id)
    product.update(**data)


@logging_decorator('products.log', 'products_logger', 'DELETE PRODUCT')
def delete_product(*args, **kwargs):
    item_id = kwargs['id']
    product = get_model_by_id_or_raise(Product, item_id)
    product.delete()
