from typing import List

from pydantic import BaseModel, Field

from app.ordered_product.schemes import OrderedProductForOrder
from app.utils.custom_types import ObjectIdStr


class BaseFields:
    id: ObjectIdStr = Field(title='ID of cart')
    id_required: ObjectIdStr = Field(..., title='ID of cart')
    total_count: int = Field(title='Total count of items in cart')
    total_count_required: int = Field(..., title='Total count of items in cart')
    total_price: float = Field(title='Total price for all items in cart')
    total_price_required: float = Field(..., title='Total price for all items in cart')
    ordered_products: List[OrderedProductForOrder] = Field()
    ordered_products_required: List[OrderedProductForOrder] = Field(...)


class AllRequired(BaseModel):
    total_count: int = BaseFields.total_count_required
    total_price: float = BaseFields.total_price_required
    ordered_products: List[OrderedProductForOrder] = BaseFields.ordered_products_required


class ResponseCreateCart(BaseModel):
    id: ObjectIdStr = BaseFields.id_required


class ResponseGetCart(AllRequired):
    id: ObjectIdStr = BaseFields.id_required

    class Config:
        orm_mode = True
        use_enum_values = True
