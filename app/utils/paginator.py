from pydantic import BaseModel
from fastapi import Query


class Paginator(BaseModel):
    limit: int = Query(1, title='Limit of result list', ge=1)
    offset: int = Query(10, title='How many items to skip', ge=1, le=200)
    select_fields: str = Query('', title='Select only necessary fields')
    # select_related: bool = Query(False, title='Select related objects')

    def paginate_model(self, pydantic_model, mongoengine_model):
        data = self.dict()
        page = data['offset']
        limit = data['limit']
        fields = [x for x in str(data['select_fields']).split(' ') if bool(x)]
        start = (page - 1) * limit
        stop = page * limit


