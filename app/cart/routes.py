
from fastapi import APIRouter

cart_router = APIRouter()


@cart_router.post('/cart')
def create_new_empty_cart():
    pass


@cart_router.get('/cart/{cart_id}')
def get_cart(cart_id: str):
    pass


@cart_router.put('/cart/{cart_id}')
def update_cart(cart_id: str):
    pass


@cart_router.delete('/cart/{cart_id}')
def delete_cart(cart_id: str):
    pass
