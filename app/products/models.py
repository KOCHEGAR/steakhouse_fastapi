from mongoengine import Document, StringField, BooleanField, FloatField, IntField
from app.enums import CookRoles
from marshmallow_mongoengine import ModelSchema


class Product(Document):
    title = StringField(required=True)
    img = StringField(default='default.jpg')
    price = FloatField(required=True)
    barcode = StringField(required=True)
    product_code = StringField(required=True)
    weight = IntField(required=True)
    measure_unit = StringField(default='г')
    description = StringField(default='Place for description...')
    status = BooleanField(default=True)
    cook_sign = StringField(default=CookRoles.steak)
    tax_rate = FloatField(default=20)

    meta = {'collection': 'products', 'strict': False}


class ProductMarshmallow(ModelSchema):
    class Meta:
        model = Product
