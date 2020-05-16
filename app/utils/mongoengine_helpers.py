from mongoengine.errors import DoesNotExist, ValidationError

from .errors import SteakhouseException


def get_model_by_id_or_raise(model, model_id, include_nested=False):
    try:
        if include_nested:
            return model.objects.get(id=model_id)
        else:
            return model.objects.no_dereference().get(id=model_id)
    except (DoesNotExist, ValidationError):
        raise SteakhouseException(f'No such element with id of ({model_id})')
