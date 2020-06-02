from typing import Optional, List

from pydantic import BaseModel, Field

from app.enums import PaymentTypes, OperationTypes
from app.ordered_product.schemes import OrderedProductForOrder
from app.utils.custom_types import ObjectIdStr
from app.utils.pagination import PaginatedResult
from .enums import AllowedStatusesToCreateOrder, AllowedStatusesToUpdateOrder


class BaseFields:
    id: ObjectIdStr = Field(title='ID of order')
    id_required: ObjectIdStr = Field(..., title='ID of order')
    cart_id: ObjectIdStr = Field(title='cart ID')
    cart_id_required: ObjectIdStr = Field(..., title='cart ID')
    on_site: bool = Field(title='Sit and eat or take and leave')
    on_site_required: bool = Field(..., title='Sit and eat or take and leave')
    order_status: AllowedStatusesToCreateOrder = Field(title='Order status')
    order_status_required: AllowedStatusesToCreateOrder = Field(..., title='Order status')
    fiscal_order_id: str = Field(title='order ID inside fiscal device')
    fiscal_order_id_required: str = Field(..., title='order ID inside fiscal device')
    operation_type: OperationTypes = Field(title='Type of operation (payment/cancel)')
    operation_type_required: OperationTypes = Field(..., title='Type of operation (payment/cancel)')
    payment_type: PaymentTypes = Field(title='Payment type')
    payment_type_required: PaymentTypes = Field(..., title='Payment type')
    payment_link: str = Field('', title='Cashless payment link')
    # payment_link_required: str = Field('', title='Cashless payment link')
    cashier_name: str = Field(title='Cashier name')
    cashier_name_required: str = Field(..., title='Cashier name')
    device_id: str = Field(title='Device id that accepted and processed order')
    device_id_required: str = Field(..., title='Device id that accepted and processed order')
    title: str = Field(title='Order title (А-21 for example)')
    title_required: str = Field(..., title='Order title (А-21 for example)')
    order_time: str = Field(title='Order creation time (from fiscal device)')
    order_time_required: str = Field(..., title='Order creation time (from fiscal device)')
    total_count: int = Field(title='Total count of product in order')
    total_count_required: int = Field(..., title='Total count of product in order')
    total_price: float = Field(title='Total price for order')
    total_price_required: float = Field(..., title='Total price for order')
    ordered_products: List[OrderedProductForOrder] = Field(title='Ordered products')
    ordered_products_required: List[OrderedProductForOrder] = Field(..., title='Ordered products')


class AllRequired(BaseModel):
    on_site: bool = BaseFields.on_site_required
    order_status: AllowedStatusesToCreateOrder = BaseFields.order_status_required
    fiscal_order_id: str = BaseFields.fiscal_order_id_required
    payment_type: PaymentTypes = BaseFields.payment_type_required
    operation_type: PaymentTypes = BaseFields.operation_type_required
    payment_link: str = BaseFields.payment_link
    cashier_name: str = BaseFields.cashier_name_required
    device_id: str = BaseFields.device_id_required
    title: str = BaseFields.title_required
    order_time: str = BaseFields.order_time_required


class AllOptional(BaseModel):
    on_site: bool = BaseFields.on_site
    order_status: AllowedStatusesToCreateOrder = BaseFields.order_status
    fiscal_order_id: str = BaseFields.fiscal_order_id
    payment_type: PaymentTypes = BaseFields.payment_type
    operation_type: PaymentTypes = BaseFields.operation_type
    payment_link: str = BaseFields.payment_link
    cashier_name: str = BaseFields.cashier_name
    device_id: str = BaseFields.device_id
    title: str = BaseFields.title
    order_time: str = BaseFields.order_time


class RequestCreateOrder(AllRequired):
    cart_id: ObjectIdStr = BaseFields.cart_id_required

    class Config:
        use_enum_values = True


class ResponseCreateOrder(AllRequired):
    id: ObjectIdStr = BaseFields.id_required
    ordered_products: List[OrderedProductForOrder] = BaseFields.ordered_products_required

    class Config:
        use_enum_values = True


class ResponseGetOrder(ResponseCreateOrder):
    pass


class RequestUpdateOrder(BaseModel):
    on_site: Optional[bool] = BaseFields.on_site
    order_status: Optional[AllowedStatusesToUpdateOrder] = BaseFields.order_status

    class Config:
        use_enum_values = True


class ResponseGetOrders(AllOptional):
    id: ObjectIdStr = BaseFields.id_required

    class Config:
        use_enum_values = True
        orm_mode = True


class ListOfOrders(PaginatedResult):
    result: List[ResponseGetOrders]
