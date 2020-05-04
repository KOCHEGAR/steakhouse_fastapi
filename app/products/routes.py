from fastapi import APIRouter

products_router = APIRouter()


@products_router.get('/products')
def get_products():
    pass


@products_router.post('/products')
def create_product():
    pass


@products_router.get('/products/{product_id}')
def get_product(product_id):
    pass


@products_router.put('/products/{product_id}')
def update_product(product_id):
    pass


@products_router.delete('/products/{product_id}')
def delete_product(product_id):
    pass
