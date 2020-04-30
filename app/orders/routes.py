from fastapi import APIRouter
from .models import RequestCreateOrder, Order

orders_router = APIRouter()

_id = 3939390015


# @orders_router.get('/orders')
# async def get_orders():
#     pass


# @orders_router.post('/orders', response_model=OrderSerializer.response_model)
@orders_router.post('/orders')
async def create_order(order: RequestCreateOrder):
    r = Order(**order.dict())
    print(await r.save())
    print(r.dict())

    return


# @orders_router.put('/orders')
# async def update_order():
#     pass


# @orders_router.delete('/orders/{order_id}')
# async def delete_order(order_id: str):
#     print('id to delete -> ', order_id)
#     pass
