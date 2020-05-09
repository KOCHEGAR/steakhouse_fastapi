from typing import List
from .schemes import ListOfProducts
from app.helpers import DocInfo


doc_get_products = DocInfo(
    descr='Get list of products',
    summ='Get products',
    res_descr='List of products',
    resp_model=ListOfProducts,
    response_model_exclude_unset=True
).__dict__
