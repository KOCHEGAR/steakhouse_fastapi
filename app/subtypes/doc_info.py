from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.utils.documentation import DocInfo
from .schemes import ResponseGetSubtype, ListOfSubtypes, ResponseCreateSubtype, ResponseGetSubtypeProducts

doc_get_subtype = DocInfo(
    descr='Get Subtype',
    summ='Get Subtype',
    res_descr='Subtype',
    resp_model=ResponseGetSubtype
).__dict__

doc_get_subtypes = DocInfo(
    descr='Get Subtypes',
    summ='Get Subtypes',
    res_descr='Subtypes',
    resp_model=ListOfSubtypes,
    response_model_exclude_unset=True
).__dict__

doc_update_subtype = DocInfo(
    descr='Update subtype',
    summ='Update subtype',
    res_descr='Subtype is updated',
    # resp_model=ResponseUpdateSubtype,
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_delete_subtype = DocInfo(
    descr='Delete subtype',
    summ='Delete subtype',
    res_descr='Subtype is deleted',
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_create_subtype = DocInfo(
    descr='Create subtype',
    summ='Create subtype',
    res_descr='Created subtype',
    resp_model=ResponseCreateSubtype,
    status_code=HTTP_201_CREATED
).__dict__

doc_get_subtype_products = DocInfo(
    descr='Get subtype products',
    summ='Get subtype products',
    res_descr='Products that attached to this subtype',
    resp_model=ResponseGetSubtypeProducts
).__dict__

doc_add_product_to_subtype = DocInfo(
    descr='Add product to subtype',
    summ='Add product to subtype',
    res_descr='Product is added to subtype',
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_delete_product_from_subtype = DocInfo(
    descr='Delete product from subtype',
    summ='Delete product from subtype',
    res_descr='Product is deleted from subtype',
    status_code=HTTP_204_NO_CONTENT
).__dict__
