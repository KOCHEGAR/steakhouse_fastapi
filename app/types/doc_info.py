from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.utils.documentation import DocInfo
from .schemes import ResponseGetType, ResponseCreateType, ListOfTypes, ResponseGetTypeSubtypes

doc_get_type = DocInfo(
    descr='Get type',
    summ='Get type',
    res_descr='Type',
    resp_model=ResponseGetType
).__dict__

doc_get_types = DocInfo(
    descr='Get types',
    summ='Get types',
    res_descr='Types',
    resp_model=ListOfTypes,
    response_model_exclude_unset=True
).__dict__

doc_update_type = DocInfo(
    descr='Update type',
    summ='Update type',
    res_descr='Type is updated',
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_delete_type = DocInfo(
    descr='Delete type',
    summ='Delete type',
    res_descr='Type is deleted',
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_create_type = DocInfo(
    descr='Create type',
    summ='Create type',
    res_descr='Created type',
    resp_model=ResponseCreateType,
    status_code=HTTP_201_CREATED
).__dict__

doc_get_type_subtypes = DocInfo(
    descr='Get type subtypes',
    summ='Get type subtypes',
    res_descr='Subtypes that attached to this type',
    resp_model=ResponseGetTypeSubtypes
).__dict__

doc_add_subtype_to_type = DocInfo(
    descr='Add subtype to type',
    summ='Add subtype to type',
    res_descr='Subtype is added to type',
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_delete_subtype_from_type = DocInfo(
    descr='Delete subtype from type',
    summ='Delete subtype from type',
    res_descr='Subtype is deleted from type',
    status_code=HTTP_204_NO_CONTENT
).__dict__
