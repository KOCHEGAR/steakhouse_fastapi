from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
from .schemes import ListOfProducts, ResponseUpdateProduct, ResponseGetProduct, ResponseCreateProduct
from app.utils.documentation import DocInfo

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
    # response_model_exclude_unset=True
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_get_product = DocInfo(
    descr='Get product',
    summ='Get product',
    res_descr='Product',
    resp_model=ResponseGetProduct
).__dict__

doc_create_product = DocInfo(
    descr='Create product',
    summ='Create product',
    res_descr='Created product',
    resp_model=ResponseCreateProduct,
    status_code=HTTP_201_CREATED
).__dict__

doc_delete_product = DocInfo(
    descr='Delete product',
    summ='Delete product',
    res_descr='Product deleted',
    status_code=HTTP_204_NO_CONTENT
).__dict__
