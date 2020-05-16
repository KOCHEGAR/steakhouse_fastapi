from fastapi import APIRouter, Depends

from app.utils.pagination import Paginator
from . import functions as funcs
from .doc_info import doc_create_type, doc_delete_type, doc_get_type, doc_get_types, doc_update_type, \
    doc_add_subtype_to_type, doc_delete_subtype_from_type, doc_get_type_subtypes
from .schemes import RequestCreateType, RequestUpdateType

types_router = APIRouter()


@types_router.get('/types', **doc_get_types)
def get_types(paginator: Paginator = Depends()):
    kwargs = {'paginator_instance': paginator}
    return funcs.get_types(**kwargs)


@types_router.post('/types', **doc_create_type)
def create_type(data: RequestCreateType):
    kwargs = {'data': data.dict()}
    return funcs.create_type(**kwargs)


@types_router.get('/types/{type_id}', **doc_get_type)
def get_type(type_id: str):
    kwargs = {'id': type_id}
    return funcs.get_type(**kwargs)


@types_router.put('/types/{type_id}', **doc_update_type)
def update_type(type_id: str, data: RequestUpdateType):
    kwargs = {'id': type_id, 'data': data.dict(exclude_none=True, exclude_unset=True)}
    funcs.update_type(**kwargs)


@types_router.delete('/types/{type_id}', **doc_delete_type)
def delete_type(type_id: str):
    kwargs = {'id': type_id}
    funcs.delete_type(**kwargs)


@types_router.get('/types/{type_id}/subtypes', **doc_get_type_subtypes)
def get_subtypes_in_type(type_id: str):
    kwargs = {'id': type_id}
    return funcs.get_subtypes_in_type(**kwargs)


@types_router.post('/types/{type_id}/subtypes/{subtype_id}', )
def add_subtype_to_type(type_id: str, subtype_id: str):
    kwargs = {'type_id': type_id, 'subtype_id': subtype_id}
    funcs.add_subtype_to_type(**kwargs)


@types_router.delete('/types/{type_id}/subtypes/{subtype_id}', )
def remove_subtype_from_type(type_id: str, subtype_id: str):
    kwargs = {'type_id': type_id, 'subtype_id': subtype_id}
    funcs.remove_subtype_from_type(**kwargs)
