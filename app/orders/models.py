from mongoengine import Document, BooleanField, StringField, DateTimeField, \
    FloatField, ReferenceField, IntField


class Order(Document):
    on_site = BooleanField(required=True)
    order_status = StringField(required=True)
    fiscal_order_id = StringField(required=True)
    payment_type = StringField(required=True)
    payment_link = StringField(default='')
    cashier_name = StringField(required=True)
    device_id = StringField(required=True)
    title = StringField(required=True)
    order_time = DateTimeField(required=True)

    total_count = IntField(required=True)
    total_price = FloatField(required=True)

    # ordered_products

    meta = {'collection': 'orders', 'strict': False}
