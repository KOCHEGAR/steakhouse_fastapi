from .schemes import ListOfProducts, ResponseUpdateProduct
from ..utils.documentation import DocInfo

doc_get_products = DocInfo(
    descr='Get list of products',
    summ='Get products',
    res_descr='List of products',
    resp_model=ListOfProducts,
    response_model_exclude_unset=True
).__dict__

doc_update_product = DocInfo(
    descr='Update Product',
    summ='Update product',
    res_descr='Updated Product',
    resp_model=ResponseUpdateProduct,
    # response_model_exclude_unset=True
).__dict__
