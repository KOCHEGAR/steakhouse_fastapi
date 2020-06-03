from mongoengine import Document, FloatField, ReferenceField, IntField, ListField, PULL

from app.ordered_product.models import OrderedProduct


class Cart(Document):
    total_count = IntField(default=0)
    total_price = FloatField(default=0)
    ordered_products = ListField(ReferenceField(OrderedProduct, reverse_delete_rule=PULL), default=[])

    meta = {'collection': 'shopping_carts', 'strict': False}

    def is_product_in_cart(self, product_id):
        ids = [op['product']['id'] for op in self.ordered_products]
        return product_id in ids

    def add_new_ordered_product(self, ordered_product):
        self.modify(push__ordered_products=ordered_product)
        self._calculate()

    def _calculate(self):
        total_count = 0
        total_price = 0
        for op in self.ordered_products:
            total_count += op.amount_total
            total_price += op.product['price'] * op.amount_total

        self.modify(total_price=total_price, total_count=total_count)

