from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field
from fastapi import Query


# For easy building openapi arguments for endpoints
class DocInfo:
    def __init__(self, descr='', summ='', res_descr='', status_code=200, resp_model=None, **kwargs):
        self.description = descr
        self.summary = summ
        self.response_description = res_descr
        self.status_code = status_code
        self.response_model = resp_model
        # self.response_model_exclude_unset = True

        # for key, val in kwargs.items():
        #     setattr(self, key, val)


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")
        return str(v)


class PaginatedResult(BaseModel):
    next: int = Field(..., title='Next page (-1 if there is nowhere to paginate)')
    prev: int = Field(..., title='Previous page (-1 if there is nowhere to paginate)')
    total: int = Field(..., title='Total amount of results')


class Pag(BaseModel):
    # sort:
    limit: int = Query(200, title='Limit!', ge=1, le=200)
    offset: int = Query(1, title='Offset!', ge=1)
    select_fields: str = Query('', title='Comma-separated list of fields to retrieve')

    def dict(self, **kwargs):
        data = super().dict(**kwargs)
        return {'pagination_data': data}


def paginate_model(pagination, marshmallow_model):
    page = pagination['offset']
    limit = pagination['limit']
    fields = str(pagination['select_fields']).split(',')
    start = (page - 1) * limit
    stop = page * limit

    mongo_model = marshmallow_model.Meta.model
    models = mongo_model.objects()[start:stop]
    total_count_of_models = models.count()
    marshmallow_kwargs = {'many': True}

    if fields:
        model_fields = list(mongo_model._fields.keys())
        for field in fields:
            if field in model_fields:
                marshmallow_kwargs.setdefault('only', []).append(field)

    models_to_response = marshmallow_model(**marshmallow_kwargs).dump(models).data
    pagination_result = {
        'next': page + 1 if stop < total_count_of_models else -1,
        'prev': page - 1 if start > 0 and stop < total_count_of_models else -1,
        'total': total_count_of_models,
        'result': models_to_response
    }
    return pagination_result
