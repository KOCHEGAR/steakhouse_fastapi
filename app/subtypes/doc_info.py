from app.utils.documentation import DocInfo
from starlette.status import HTTP_201_CREATED
from .schemes import ResponseGetSubtype, ListOfSubtypes, ResponseUpdateSubtype, \
    ResponseDeleteSubtype, ResponseCreateSubtype

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
    res_descr='Updated subtype',
    resp_model=ResponseUpdateSubtype
).__dict__

doc_delete_subtype = DocInfo(
    descr='Delete subtype',
    summ='Delete subtype',
    res_descr='ID of deleted subtype',
    resp_model=ResponseDeleteSubtype
).__dict__

doc_create_subtype = DocInfo(
    descr='Create subtype',
    summ='Create subtype',
    res_descr='Created subtype',
    resp_model=ResponseCreateSubtype,
    status_code=HTTP_201_CREATED
).__dict__
