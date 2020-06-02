from mongoengine import Document, FloatField, ReferenceField, IntField, ListField, PULL

from app.ordered_product.models import OrderedProduct


class Cart(Document):
    total_count = IntField(default=0)
    total_price = FloatField(default=0)
    ordered_products = ListField(ReferenceField(OrderedProduct, reverse_delete_rule=PULL))

    meta = {'collection': 'shopping_carts', 'strict': False}
