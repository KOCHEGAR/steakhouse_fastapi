from marshmallow_mongoengine import ModelSchema, fields
from mongoengine import Document, StringField, BooleanField, ReferenceField, ListField, PULL

from app.products.models import Product, ProductMarshmallow


class Subtype(Document):
    title = StringField(required=True)
    status = BooleanField(default=False)
    products = ListField(ReferenceField(Product, reverse_delete_rule=PULL), default=[])

    meta = {'collection': 'subtypes', 'strict': False}

    def check_presence(self, product_instance):
        return product_instance in self.products

    def get_products(self):
        return self.products

    def add_product(self, product_instance):
        self.modify(push__products=product_instance)

    def remove_product(self, product_instance):
        self.modify(pull__products=product_instance)


class SubtypeMarshmallowModel(ModelSchema):
    products = fields.Nested(ProductMarshmallow, many=True)

    class Meta:
        model = Subtype
