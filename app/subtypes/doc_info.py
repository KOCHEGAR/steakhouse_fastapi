from .schemes import SubtypeForGetSubtype, ListOfSubtypes
from ..utils.documentation import DocInfo

doc_get_subtype = DocInfo(
    descr='Get Subtype',
    summ='Get Subtype',
    res_descr='Subtype',
    resp_model=SubtypeForGetSubtype
).__dict__

doc_get_subtypes = DocInfo(
    descr='Get Subtypes',
    summ='Get Subtypes',
    res_descr='Subtypes',
    resp_model=ListOfSubtypes,
    response_model_exclude_unset=True
).__dict__
