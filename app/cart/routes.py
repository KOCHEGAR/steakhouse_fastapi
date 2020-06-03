from fastapi import APIRouter
from . import functions

from .doc_info import doc_get_cart, doc_create_cart, doc_delete_cart, doc_add_to_cart, doc_remove_from_cart

cart_router = APIRouter()


@cart_router.post('/cart', **doc_create_cart)
def create_cart():
    return functions.create_cart()


@cart_router.get('/cart/{cart_id}', **doc_get_cart)
def get_cart(cart_id: str):
    kwargs = {'id': cart_id}
    return functions.get_cart(**kwargs)


@cart_router.post('/cart/{cart_id}/add/{product_id}/{quantity}', **doc_add_to_cart)
def add_to_cart(cart_id: str, product_id: str, quantity: int):
    kwargs = {'cart_id': cart_id, 'product_id': product_id, 'quantity': quantity}
    functions.add_to_cart(**kwargs)


@cart_router.post('/cart/{cart_id}/remove/{product_id}/{quantity}', **doc_remove_from_cart)
def remove_from_cart(cart_id: str, product_id: str, quantity: int):
    kwargs = {'cart_id': cart_id, 'product_id': product_id, 'quantity': quantity}
    functions.remove_from_cart(**kwargs)


@cart_router.delete('/cart/{cart_id}', **doc_delete_cart)
def delete_cart(cart_id: str):
    kwargs = {'id': cart_id}
    functions.delete_cart(**kwargs)
