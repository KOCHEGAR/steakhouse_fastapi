from typing import List
from app.helpers import DocInfo
from .schemes import SubtypeForGetSubtype, SubtypeForGetSubtypes, ListOfSubtypes


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
