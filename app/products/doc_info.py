from typing import List
from .schemes import Product
from app.helpers import DocInfo, PaginatedResult


class ListOfProducts(PaginatedResult):
    result: List[Product]


doc_get_products = DocInfo(
    descr='Get list of products',
    summ='Get products',
    res_descr='List of products',
    resp_model=ListOfProducts
).__dict__
