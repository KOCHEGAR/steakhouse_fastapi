from mongoengine import Document, StringField, BooleanField, ReferenceField, ListField, PULL

from app.subtypes.models import Subtype


class Type(Document):
    title = StringField(required=True)
    status = BooleanField(default=False)
    is_promo = BooleanField(default=False)
    subtypes = ListField(ReferenceField("Subtype", reverse_delete_rule=PULL), default=[])

    meta = {'collection': 'types', 'strict': False}

    def check_presence(self, subtype):
        return subtype in self.subtypes

    def get_subtypes(self):
        return self.subtypes

    def add_subtype(self, subtype):
        self.modify(push__subtypes=subtype)

    def remove_subtype(self, subtype):
        self.modify(pull__subtypes=subtype)
