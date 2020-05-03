from mongoengine import Document, BooleanField, StringField, DictField, IntField


class OrderedProduct(Document):
    status = StringField()
    amount_total = IntField(default=1)
    amount_ready = IntField(default=0)
    amount_given = IntField(default=0)
    on_site = BooleanField(default=True)
    product = DictField(required=True)

    meta = {'collection': 'ordered_products', 'strict': False}


