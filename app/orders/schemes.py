
from pydantic import BaseModel, Field
from typing import Optional
from app.enums import PaymentTypes
from .enums import AllowedStatusesToCreateOrder, AllowedStatusesToUpdateOrder


class RequestCreateOrder(BaseModel):
    on_site: bool = Field(True, title='С собой или на месте')
    cart_id: str = Field(..., title='ID корзины')
    order_status: AllowedStatusesToCreateOrder = Field(..., title='Статус заказа')
    fiscal_order_id: str = Field(..., title='ID заказа из фискальника')
    payment_type: PaymentTypes = Field(..., title='Тип оплаты')
    payment_link: str = Field('', title='Ссылка безналичного платежа')
    cashier_name: str = Field(..., title='Имя кассира')
    device_id: str = Field(..., title='ID устройства, с которого был сделан заказ')
    title: str = Field(..., title='Обозначение заказа (А-21 например)')
    order_time: str = Field(..., title='Время создания заказа')

    class Config:
        use_enum_values = True


class RequestUpdateOrder(BaseModel):
    on_site: Optional[bool] = Field(title='С собой или на месте')
    order_status: Optional[AllowedStatusesToUpdateOrder] = Field(title='Статус заказа')

    class Config:
        use_enum_values = True
