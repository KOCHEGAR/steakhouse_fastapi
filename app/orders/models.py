from fastapi_contrib.db.models import MongoDBModel
from pydantic import Field, BaseModel
from app.enums import OrderStatuses, PaymentTypes, OperationTypes, OperationTypePayment
# from
from fastapi_contrib.serializers import openapi
from fastapi_contrib.serializers.common import Serializer


class OrderSchema(BaseModel):
    time_ordered: str = Field(..., title='Time from fiscal device')
    total_price: float = Field(..., title='Total price for order (from fiscal device)')
    status: OrderStatuses = Field(..., title='Cooking order status')
    on_site: bool = Field(True, title='Eat here, or not here')
    title: str = Field(..., title='Readable order name')
    cashier_name: str = Field(..., title='Cashier who made order')
    payment_type: PaymentTypes = Field(...)
    operation_type: OperationTypes = Field(OperationTypes.payment)


class Order(OrderSchema, MongoDBModel):
    class Meta:
        collection = 'orders'
# class Order(MongoDBModel):
#     time_ordered: str = Field(..., title='Time from fiscal device')
#     total_price: float = Field(..., title='Total price for order (from fiscal device)')
#     status: OrderStatuses = Field(..., title='Cooking order status')
#     on_site: bool = Field(True, title='Eat here, or not here')
#     title: str = Field(..., title='Readable order name')
#     cashier_name: str = Field(..., title='Cashier who made order')
#     payment_type: PaymentTypes = Field(...)
#     operation_type: OperationTypes = Field(...)
#
#     class Meta:
#         collection = 'orders'


# class RequestCreateOrder(OrderSchema):
#     operation_type: OperationTypePayment
#     pass




@openapi.patch
class RequestCreateOrder(Serializer):
    class Meta:
        model = Order
        read_only_fields = {'id', 'operation_type'}
RequestCreateOrder.__doc__ = ''


# @openapi.patch
# class OrderSerializer(Serializer):
#
#     class Meta:
#         model = Order
#         read_only_fields = {'id'}


# RequestCreateOrder.__doc__ = ''


# class ResponseCreateOrder(BaseModel):
#     time_ordered: str = Field(..., title='Time from fiscal device')
#     status: OrderStatuses = Field(..., title='Cooking order status')
