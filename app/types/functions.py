from app.subtypes.models import Subtype
from app.utils.errors import SteakhouseException
from app.utils.logging import logging_decorator
from app.utils.mongoengine_helpers import get_model_by_id_or_raise
from .models import Type
from .schemes import ResponseGetTypes


def create_dummy_items():
    from uuid import uuid4

    for i in range(5):
        p = Type()
        p.title = f'item_{str(uuid4())}_{i}'
        p.save()


@logging_decorator('types.log', 'types_logger', 'GET TYPES')
def get_types(*args, **kwargs):
    return kwargs['paginator_instance'].paginate_model(ResponseGetTypes, Type)


@logging_decorator('types.log', 'types_logger', 'CREATE TYPE')
def create_type(*args, **kwargs):
    data = kwargs['data']
    return Type(**data).save()


@logging_decorator('types.log', 'types_logger', 'GET TYPE')
def get_type(*args, **kwargs):
    item_id = kwargs['id']
    return get_model_by_id_or_raise(Type, item_id)


@logging_decorator('types.log', 'types_logger', 'UPDATE TYPE')
def update_type(*args, **kwargs):
    item_id = kwargs['id']
    data = kwargs['data']

    if not data:
        raise SteakhouseException(f'Empty data to update')

    _type = get_model_by_id_or_raise(Type, item_id)
    _type.update(**data)


@logging_decorator('types.log', 'types_logger', 'DELETE TYPE')
def delete_type(*args, **kwargs):
    item_id = kwargs['id']

    _type = get_model_by_id_or_raise(Type, item_id)
    _type.delete()


@logging_decorator('types.log', 'types_logger', 'GET SUBTYPES IN TYPE')
def get_subtypes_in_type(*args, **kwargs):
    item_id = kwargs['id']
    _type = get_model_by_id_or_raise(Type, item_id, include_nested=True)
    return _type


@logging_decorator('types.log', 'types_logger', 'ADD SUBTYPE TO TYPE')
def add_subtype_to_type(*args, **kwargs):
    _type, subtype = _add_or_remove(**kwargs)

    if _type.check_presence(subtype):
        raise SteakhouseException('That subtype already in this type')

    _type.add_subtype(subtype)


@logging_decorator('types.log', 'types_logger', 'REMOVE SUBTYPE FROM TYPE')
def remove_subtype_from_type(*args, **kwargs):
    _type, subtype = _add_or_remove(**kwargs)

    if not _type.check_presence(subtype):
        raise SteakhouseException('That subtype not found in this type')

    _type.remove_subtype(subtype)


def _add_or_remove(**kwargs):
    type_id = kwargs['type_id']
    subtype_id = kwargs['subtype_id']
    subtype = get_model_by_id_or_raise(Subtype, subtype_id)
    _type = get_model_by_id_or_raise(Type, type_id, include_nested=True)
    return _type, subtype
