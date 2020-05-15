from typing import List

from fastapi import Query
from pydantic import BaseModel, Field


class PaginatedResult(BaseModel):
    next: int = Field(..., title='Next page (-1 if there is nowhere to paginate)')
    prev: int = Field(..., title='Previous page (-1 if there is nowhere to paginate)')
    total: int = Field(..., title='Total amount of results')


class Paginator(BaseModel):
    limit: int = Query(10, title='Limit of result list', ge=1, le=200)
    offset: int = Query(1, title='How many items to skip', ge=1)
    select_fields: str = Query('', title='Select only necessary fields')

    def paginate_model(self, pydantic_model, mongoengine_model):
        data = self.dict()
        page = data['offset']
        limit = data['limit']
        fields = self._return_list_of_valid_fields(data['select_fields'], pydantic_model)
        start = (page - 1) * limit
        stop = page * limit

        models = mongoengine_model.objects.only(*fields).no_dereference()[start:stop]
        total_count_of_models = models.count()

        result = [
            pydantic_model.from_orm(model).dict(include=set(fields) or None)
            for model in models
        ]

        pagination_result = {
            'next': page + 1 if stop < total_count_of_models else -1,
            'prev': page - 1 if start > 0 and stop < total_count_of_models else -1,
            'total': total_count_of_models,
            'result': result
        }
        return pagination_result

    def _return_list_of_valid_fields(self, selected_fields, pydantic_model):
        fields = [x for x in str(selected_fields).split(' ') if bool(x)]

        if not fields:
            return []

        actual_fields = list(pydantic_model.__fields__.keys())

        valid_fields = [field for field in fields if field in actual_fields]

        if valid_fields and ('id' not in valid_fields):
            valid_fields.append('id')

        return valid_fields
