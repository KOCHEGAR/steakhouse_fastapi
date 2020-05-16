from app.products.models import Product
from app.utils.errors import SteakhouseException
from app.utils.mongoengine_helpers import get_model_by_id_or_raise
from .models import Subtype
from .schemes import ResponseGetSubtypes


def create_dummy_subtypes():
    from uuid import uuid4

    for i in range(5):
        p = Subtype()
        p.title = f'item_{str(uuid4())}_{i}'
        p.save()


def get_subtypes(*args, **kwargs):
    return kwargs['paginator_instance'].paginate_model(ResponseGetSubtypes, Subtype)


def create_subtype(*args, **kwargs):
    data = kwargs['data']
    return Subtype(**data).save()


def get_subtype(*args, **kwargs):
    item_id = kwargs['id']
    return get_model_by_id_or_raise(Subtype, item_id)


def update_subtype(*args, **kwargs):
    item_id = kwargs['id']
    data = kwargs['data']

    if not data:
        raise SteakhouseException(f'Empty data to update')

    subtype = get_model_by_id_or_raise(Subtype, item_id)
    subtype.update(**data)


def delete_subtype(*args, **kwargs):
    item_id = kwargs['id']

    subtype = get_model_by_id_or_raise(Subtype, item_id)
    subtype.delete()


def get_products_in_subtype(*args, **kwargs):
    item_id = kwargs['id']
    subtype = get_model_by_id_or_raise(Subtype, item_id, include_nested=True)
    return subtype


def add_product_to_subtype(*args, **kwargs):
    subtype, product = _add_or_remove(**kwargs)

    if subtype.check_presence(product):
        raise SteakhouseException('That product already in this subtype')

    subtype.add_product(product)


def remove_product_from_subtype(*args, **kwargs):
    subtype, product = _add_or_remove(**kwargs)

    if not subtype.check_presence(product):
        raise SteakhouseException('That product not found in this subtype')

    subtype.remove_product(product)


def _add_or_remove(**kwargs):
    subtype_id = kwargs['subtype_id']
    product_id = kwargs['product_id']
    product = get_model_by_id_or_raise(Product, product_id)
    subtype = get_model_by_id_or_raise(Subtype, subtype_id, include_nested=True)
    return subtype, product
