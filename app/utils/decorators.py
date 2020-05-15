from functools import wraps
from .errors import SteakhouseException


def check_existence_by_id(func):
    @wraps(func)
    def wrapper(item_id):
        try:
            return func(item_id)
        except Exception as e:
            pass
            raise SteakhouseException(f'No such item with id ({item_id})', code=400)

    return wrapper
