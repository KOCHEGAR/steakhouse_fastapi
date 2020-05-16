from fastapi import APIRouter, Depends

from app.utils.pagination import Paginator
from . import functions as funcs
from .doc_info import doc_get_subtype, doc_get_subtypes, doc_update_subtype, \
    doc_delete_subtype, doc_create_subtype, doc_get_subtype_products, \
    doc_add_product_to_subtype, doc_delete_product_from_subtype
from .schemes import RequestUpdateSubtype, RequestCreateSubtype

subtypes_router = APIRouter()


@subtypes_router.get('/subtypes', **doc_get_subtypes)
def get_subtypes(paginator: Paginator = Depends()):
    kwargs = {'paginator_instance': paginator}
    return funcs.get_subtypes(**kwargs)


@subtypes_router.post('/subtypes', **doc_create_subtype)
def create_subtype(data: RequestCreateSubtype):
    data = {'data': data.dict()}
    return funcs.create_subtype(**data)


@subtypes_router.get('/subtypes/{subtype_id}', **doc_get_subtype)
def get_subtype(subtype_id: str):
    data = {'id': subtype_id}
    return funcs.get_subtype(**data)


@subtypes_router.put('/subtypes/{subtype_id}', **doc_update_subtype)
def update_subtype(subtype_id: str, data: RequestUpdateSubtype):
    data = {'id': subtype_id, 'data': data.dict(exclude_none=True, exclude_unset=True)}
    funcs.update_subtype(**data)


@subtypes_router.delete('/subtypes/{subtype_id}', **doc_delete_subtype)
def delete_subtype(subtype_id: str):
    data = {'id': subtype_id}
    funcs.delete_subtype(**data)


@subtypes_router.get('/subtypes/{subtype_id}/products', **doc_get_subtype_products)
def get_products_in_subtype(subtype_id):
    data = {'id': subtype_id}
    return funcs.get_products_in_subtype(**data)


@subtypes_router.post('/subtypes/{subtype_id}/products/{product_id}', **doc_add_product_to_subtype)
def add_product_to_subtype(subtype_id: str, product_id: str):
    data = {'subtype_id': subtype_id, 'product_id': product_id}
    funcs.add_product_to_subtype(**data)


@subtypes_router.delete('/subtypes/{subtype_id}/products/{product_id}', **doc_delete_product_from_subtype)
def remove_product_from_subtype(subtype_id: str, product_id: str):
    data = {'subtype_id': subtype_id, 'product_id': product_id}
    funcs.remove_product_from_subtype(**data)
