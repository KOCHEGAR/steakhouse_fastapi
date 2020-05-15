from typing import Optional, List

from pydantic import BaseModel, Field

from app.enums import PaymentTypes
from app.ordered_product.schemes import OrderedProductForCreatedOrder
from .enums import AllowedStatusesToCreateOrder, AllowedStatusesToUpdateOrder


class BaseFields:
    cart_id: str = Field(..., title='cart ID')
    on_site: bool = Field(True, title='Sit and eat or take and leave')
    order_status: AllowedStatusesToCreateOrder = Field(..., title='Order status')
    fiscal_order_id: str = Field(..., title='order ID inside fiscal device')
    payment_type: PaymentTypes = Field(..., title='Payment type')
    payment_link: str = Field('', title='Cashless payment link')
    cashier_name: str = Field(..., title='Cashier name')
    device_id: str = Field(..., title='Device id that accepted and processed order')
    title: str = Field(..., title='Order title (А-21 for example)')
    order_time: str = Field(..., title='Order creation time (from fiscal device)')
    total_count: int = Field(..., title='Total count of product in order')
    total_price: float = Field(..., title='Total price for order')
    # ordered_products: List[OrderedProductForCreatedOrder] = Field(..., title='Ordered products')


# class OrderSchema(BaseModel):
#     pass
# on_site: bool = Field(True, title='С собой или на месте')
# cart_id: bool = Field(..., title='ID корзины')
# order_status: AllowedStatusesToCreateOrder = Field(..., title='Статус заказа')
# fiscal_order_id: str = Field(..., title='ID заказа из фискальника')
# payment_type: PaymentTypes = Field(..., title='Тип оплаты')
# payment_link: str = Field('', title='Ссылка безналичного платежа')
# cashier_name: str = Field(..., title='Имя кассира')
# device_id: str = Field(..., title='ID устройства, с которого был сделан заказ')
# title: str = Field(..., title='Обозначение заказа (А-21 например)')
# order_time: str = Field(..., title='Время создания заказа')


class RequestCreateOrder(BaseModel):
    cart_id: str = BaseFields.cart_id
    on_site: bool = BaseFields.on_site
    order_status: AllowedStatusesToCreateOrder = BaseFields.order_status
    fiscal_order_id: str = BaseFields.fiscal_order_id
    payment_type: PaymentTypes = BaseFields.payment_type
    payment_link: str = BaseFields.payment_link
    cashier_name: str = BaseFields.cashier_name
    device_id: str = BaseFields.device_id
    title: str = BaseFields.title
    order_time: str = BaseFields.order_time

    class Config:
        use_enum_values = True


class ResponseCreateOrder(BaseModel):
    on_site: bool = BaseFields.on_site
    order_status: AllowedStatusesToCreateOrder = BaseFields.order_status
    fiscal_order_id: str = BaseFields.fiscal_order_id
    payment_type: PaymentTypes = BaseFields.payment_type
    payment_link: str = BaseFields.payment_link
    cashier_name: str = BaseFields.cashier_name
    device_id: str = BaseFields.device_id
    title: str = BaseFields.title
    order_time: str = BaseFields.order_time
    total_count: int = BaseFields.total_count
    total_price: float = BaseFields.total_price
    ordered_products: List[OrderedProductForCreatedOrder] = Field(..., title='Ordered products')

    class Config:
        use_enum_values = True


class ResponseGetOrder(ResponseCreateOrder):
    pass


class RequestUpdateOrder(BaseModel):
    on_site: Optional[bool] = Field(title='С собой или на месте')
    order_status: Optional[AllowedStatusesToUpdateOrder] = Field(title='Статус заказа')

    class Config:
        use_enum_values = True
