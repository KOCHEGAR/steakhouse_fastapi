from mongoengine import Document, BooleanField, FloatField, ReferenceField, IntField
from pydantic import BaseModel, Field


class ShoppingCart(Document):
    total_count = IntField(default=0)
    total_price = FloatField(default=0)
    # ordered_products = ReferenceField()

    meta = {'collection': 'shopping_carts', 'strict': False}
