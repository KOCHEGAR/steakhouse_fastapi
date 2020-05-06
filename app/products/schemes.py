from pydantic import BaseModel, Field
# from typing import Optional
from app.enums import CookRoles


class BaseFields:
    title: str = Field(..., title='Product title', min_length=3)
    img: str = Field('default.jpg', title='Product image')
    price: float = Field(..., title='Product price (in RUB)')
    barcode: str = Field(..., title='Product barcode')
    product_code: str = Field(..., title='Product code')
    weight: int = Field(..., title='Product weight (2000 = 2 kg/liter, for example)')
    measure_unit: str = Field('г', title='Product measure unit')
    description: str = Field('Place for description...', title='Product description')
    status_active: bool = Field(True, title='Product visibility')
    cook_sign: CookRoles = Field(..., title='Who will prepare this')


class Product(BaseModel):
    title: str = BaseFields.title
    img: str = BaseFields.img
    price: float = BaseFields.price
    barcode: str = BaseFields.barcode
    product_code: str = BaseFields.product_code
    weight: int = BaseFields.weight
    measure_unit: str = BaseFields.measure_unit
    description: str = BaseFields.description
    status_active: bool = BaseFields.status_active
    cook_sign: CookRoles = BaseFields.cook_sign

    class Config:
        use_enum_values = True
        orm_mode = True


class ProductForCreatedOrder(BaseModel):
    barcode: str = BaseFields.barcode
    product_code: str = BaseFields.product_code
    title: str = BaseFields.title
    cook_sign: CookRoles = BaseFields.cook_sign

    class Config:
        use_enum_values = True
