from marshmallow_mongoengine import ModelSchema, fields
from mongoengine import Document, StringField, BooleanField, ReferenceField, ListField, PULL

from app.products.models import Product, ProductMarshmallow


class Subtype(Document):
    title = StringField(required=True)
    status = BooleanField(default=False)
    products = ListField(ReferenceField(Product, reverse_delete_rule=PULL), default=[])

    meta = {'collection': 'subtypes', 'strict': False}

    def _check_presence(self, product_instance):
        return product_instance in self.products

    def add_product(self, product_instance):
        self.products.append(product_instance)
        self.save()

    def remove_product(self, product_instance):
        pass


class SubtypeMarshmallowModel(ModelSchema):
    products = fields.Nested(ProductMarshmallow, many=True)

    class Meta:
        model = Subtype
