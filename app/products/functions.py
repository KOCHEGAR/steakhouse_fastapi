from .models import Product
from app.helpers import paginate_model


def create_dummy_products():
    from random import randint
    from uuid import uuid4

    for i in range(2000):
        p = Product()
        p.title = f'item_{str(uuid4())}_{i}'
        p.barcode = str(randint(200000, 3000000))
        p.product_code = str(randint(400000, 500000))
        p.price = float(randint(20, 300))
        p.weight = randint(50, 1000)
        p.save()


def get_products(*args, **kwargs):
    return paginate_model(kwargs['pagination_data'], Product)

