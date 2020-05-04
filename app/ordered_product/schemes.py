from pydantic import BaseModel, Field
from app.enums import OrderedProductStatuses
from app.products.schemes import ProductForCreatedOrder


class BaseFields:
    status: OrderedProductStatuses = Field(..., title='What status of the dish in order')
    amount_total: int = Field(1, title='Amount of actual product in order', ge=1)
    amount_ready: int = Field(0, title='Amount ready now', ge=0)
    amount_given: int = Field(0, title='Amount given to client already', ge=0)
    on_site: bool = Field(True, title='Sit and eat in place, or take it and leave')


class OrderedProduct(BaseModel):
    status: OrderedProductStatuses = BaseFields.status
    amount_total: int = BaseFields.amount_total
    amount_ready: int = BaseFields.amount_ready
    amount_given: int = BaseFields.amount_given
    on_site: bool = BaseFields.on_site
    # product = Field()

    class Config:
        use_enum_values = True


class OrderedProductForCreatedOrder(BaseModel):
    status: OrderedProductStatuses = BaseFields.status
    amount_total: int = BaseFields.amount_total
    amount_ready: int = BaseFields.amount_ready
    amount_given: int = BaseFields.amount_given
    on_site: bool = BaseFields.on_site
    product: ProductForCreatedOrder = Field(...)

    class Config:
        use_enum_values = True
