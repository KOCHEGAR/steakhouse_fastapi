from app.utils.errors import SteakhouseException
from .models import Subtype
from .schemes import SubtypeForGetSubtypes


def create_dummy_subtypes():
    from uuid import uuid4

    for i in range(5):
        p = Subtype()
        p.title = f'item_{str(uuid4())}_{i}'
        # p.barcode = str(randint(200000, 3000000))
        # p.product_code = str(randint(400000, 500000))
        # p.price = float(randint(20, 300))
        # p.weight = randint(50, 1000)
        p.save()


def get_subtypes(*args, **kwargs):
    return kwargs['paginator_instance'].paginate_model(SubtypeForGetSubtypes, Subtype)


def create_subtype():
    pass


def get_subtype(subtype_id):
    try:
        return Subtype.objects.get(id=subtype_id)
    except Exception as e:
        raise SteakhouseException(f'No such element with id ({subtype_id})')


def update_subtype():
    pass


def delete_subtype():
    pass


def add_product_to_subtype():
    pass


def remove_product_from_subtype():
    pass
