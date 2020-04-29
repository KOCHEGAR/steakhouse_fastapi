
from fastapi import FastAPI
from fastapi_contrib.db.utils import setup_mongodb
from fastapi_contrib.conf import settings
from fastapi_contrib.db.models import MongoDBTimeStampedModel
from fastapi_contrib.serializers import openapi
from fastapi_contrib.serializers.common import Serializer
from pydantic import Field
from typing import List

app = FastAPI()
settings.mongodb_max_pool_size = 20
settings.mongodb_dbname = 'steakhouse'
settings.mongodb_dsn = 'mongodb://127.0.0.1:27017'
settings.fastapi_app = 'app.app'



class MyOrder(MongoDBTimeStampedModel):
    zipcodes: List[str] = Field([])
    order_name: str
    total_price: int = Field(..., gt=1)

    class Meta:
        collection = 'my_orders'


@openapi.patch
class MyOrderSerializer(Serializer):

    class Meta:
        model = MyOrder
        read_only_fields = {'id', 'created'}
        write_only_fields = {'zipcodes'}


MyOrderSerializer.__doc__ = ""


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/', response_model=MyOrderSerializer.response_model, status_code=201)
async def hello(order: MyOrderSerializer):
    print(type(order))
    print('income ', order)
    print(order.total_price)
    instance = await order.save()
    print(type(instance))
    print(instance.dict())
    return instance.dict()
    pass

@app.get('/orders', response_model=List[MyOrderSerializer.response_model])
async def orders():
    return await MyOrder.list()

@app.get('/{id}', response_model=MyOrderSerializer.response_model)
async def get_one(id: int):
    # MyOrderSerializer
    result = await MyOrder.get(id=id)

    print(result.dict(exclude={'zipcodes'}))
    return result
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


@app.on_event('startup')
async def startup():
    setup_mongodb(app)
