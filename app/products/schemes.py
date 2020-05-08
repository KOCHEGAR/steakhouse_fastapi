from pydantic import BaseModel, Field
from typing import Optional
from app.enums import CookRoles
from app.helpers import ObjectIdStr


# class BaseFields:
#     id: ObjectIdStr
#     title: str = Field(..., title='Product title', min_length=3)
#     img: str = Field('default.jpg', title='Product image')
#     price: float = Field(..., title='Product price (in RUB)')
#     barcode: str = Field(..., title='Product barcode')
#     product_code: str = Field(..., title='Product code')
#     weight: int = Field(..., title='Product weight (2000 = 2 kg/liter, for example)')
#     measure_unit: str = Field('г', title='Product measure unit')
#     description: str = Field('Place for description...', title='Product description')
#     status_active: bool = Field(True, title='Product visibility')
#     cook_sign: CookRoles = Field(..., title='Who will prepare this')


class BaseFields:
    id: ObjectIdStr = Field(title='ID сущности')
    id_required: ObjectIdStr = Field(title='ID сущности')
    title: str = Field(title='Product title', min_length=3)
    title_required: str = Field(..., title='Product title', min_length=3)
    img: str = Field('default.jpg', title='Product image')
    img_required: str = Field(..., title='Product image')
    price: float = Field(title='Product price (in RUB)')
    price_required: float = Field(..., title='Product price (in RUB)')
    barcode: str = Field(title='Product barcode')
    barcode_required: str = Field(..., title='Product barcode')
    product_code: str = Field(title='Product code')
    product_code_requires: str = Field(..., title='Product code')
    weight: int = Field(title='Product weight (2000 = 2 kg/liter, for example)')
    weight_required: int = Field(..., title='Product weight (2000 = 2 kg/liter, for example)')
    measure_unit: str = Field('г', title='Product measure unit')
    description: str = Field('Place for description...', title='Product description')
    description_required: str = Field(..., title='Product description')
    status_active: bool = Field(True, title='Product visibility')
    status_active_required: bool = Field(..., title='Product visibility')
    cook_sign: CookRoles = Field(title='Who will prepare this')
    cook_sign_required: CookRoles = Field(..., title='Who will prepare this')


class Product(BaseModel):
    # id: ObjectIdStr
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
    id: ObjectIdStr = BaseFields.id
    barcode: str = BaseFields.barcode
    product_code: str = BaseFields.product_code
    title: str = BaseFields.title
    cook_sign: CookRoles = BaseFields.cook_sign

    class Config:
        use_enum_values = True


class ProductForGetProducts(BaseModel):
    id: Optional[ObjectIdStr]
    title: Optional[str]
    img: Optional[str]
    price: Optional[float]
    barcode: Optional[str]
    product_code: Optional[str]
    weight: Optional[int]
    measure_unit: Optional[str]
    description: Optional[str]
    status_active: Optional[bool]
    cook_sign: Optional[CookRoles]

    class Config:
        use_enum_values = True
        # orm_mode = True
