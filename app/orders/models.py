from mongoengine import Document, BooleanField, StringField, DateTimeField, \
    FloatField, ReferenceField, IntField, ListField, PULL

from app.ordered_product.models import OrderedProduct


class Order(Document):
    # come from fiscal device
    fiscal_order_id = StringField(required=True)
    payment_type = StringField(required=True)
    payment_link = StringField(default='')
    cashier_name = StringField(required=True)
    device_id = StringField(required=True)
    title = StringField(required=True)
    order_time = DateTimeField(required=True)
    total_count = IntField(required=True)
    total_price = FloatField(required=True)

    # only app related
    on_site = BooleanField(required=True)
    order_status = StringField(required=True)
    ordered_products = ListField(ReferenceField(OrderedProduct, reverse_delete_rule=PULL))

    meta = {'collection': 'orders', 'strict': False}
