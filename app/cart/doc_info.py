from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.utils.documentation import DocInfo
from .schemes import ResponseCreateCart, ResponseGetCart

doc_create_cart = DocInfo(
    descr='Create cart',
    summ='Create cart',
    res_descr='Returned cart ID',
    resp_model=ResponseCreateCart,
    status_code=HTTP_201_CREATED
).__dict__

doc_get_cart = DocInfo(
    descr='Get cart',
    summ='Get cart',
    res_descr='Returned cart',
    resp_model=ResponseGetCart
).__dict__

doc_delete_cart = DocInfo(
    descr='Delete cart',
    summ='Delete cart',
    res_descr='Cart is deleted',
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_add_to_cart = DocInfo(
    descr='Add few items to cart',
    summ='Add few items to cart',
    res_descr='Successfully added',
    status_code=HTTP_204_NO_CONTENT
).__dict__

doc_remove_from_cart = DocInfo(
    descr='Remove few items from cart',
    summ='Remove few items from cart',
    res_descr='Successfully removed',
    status_code=HTTP_204_NO_CONTENT
).__dict__
