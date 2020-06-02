from typing import Optional, List

from pydantic import BaseModel, Field

from app.enums import CookRoles
from app.utils.custom_types import ObjectIdStr
from app.utils.pagination import PaginatedResult


class BaseFields:
    id: ObjectIdStr = Field(title='ID сущности')
    id_required: ObjectIdStr = Field(..., title='ID сущности')
    title: str = Field(title='Product title', min_length=3)
    title_required: str = Field(..., title='Product title', min_length=3)
    img: str = Field('default.jpg', title='Product image')
    img_required: str = Field(..., title='Product image')
    price: float = Field(title='Product price (in RUB)')
    price_required: float = Field(..., title='Product price (in RUB)')
    barcode: str = Field(title='Product barcode')
    barcode_required: str = Field(..., title='Product barcode')
    product_code: str = Field(title='Product code')
    product_code_required: str = Field(..., title='Product code')
    weight: int = Field(title='Product weight (2000 = 2 kg/liter, for example)')
    weight_required: int = Field(..., title='Product weight (2000 = 2 kg/liter, for example)')
    measure_unit: str = Field('г', title='Product measure unit')
    measure_unit_required: str = Field('г', title='Product measure unit')
    description: str = Field('Place for description...', title='Product description')
    description_required: str = Field(..., title='Product description')
    status: bool = Field(True, title='Product visibility')
    status_required: bool = Field(..., title='Product visibility')
    cook_sign: CookRoles = Field(title='Who will prepare this')
    cook_sign_required: CookRoles = Field(..., title='Who will prepare this')


class AllOptional(BaseModel):
    title: Optional[str] = BaseFields.title
    img: Optional[str] = BaseFields.img
    price: Optional[float] = BaseFields.price
    barcode: Optional[str] = BaseFields.barcode
    product_code: Optional[str] = BaseFields.product_code
    weight: Optional[int] = BaseFields.weight
    measure_unit: Optional[str] = BaseFields.measure_unit
    description: Optional[str] = BaseFields.description
    status: Optional[bool] = BaseFields.status
    cook_sign: Optional[CookRoles] = BaseFields.cook_sign

    class Config:
        use_enum_values = True


class AllRequired(BaseModel):
    title: str = BaseFields.title_required
    img: str = BaseFields.img_required
    price: float = BaseFields.price_required
    barcode: str = BaseFields.barcode_required
    product_code: str = BaseFields.product_code_required
    weight: int = BaseFields.weight_required
    measure_unit: str = BaseFields.measure_unit_required
    description: str = BaseFields.description_required
    status: bool = BaseFields.status_required
    cook_sign: CookRoles = BaseFields.cook_sign_required

    class Config:
        use_enum_values = True


class RequestCreateProduct(AllRequired):
    pass
    # class Config:
        # use_enum_values = True
        # orm_mode = True


class ResponseCreateProduct(AllRequired):
    id: ObjectIdStr = BaseFields.id_required

    class Config:
        orm_mode = True


class ResponseGetProduct(RequestCreateProduct):
    id: ObjectIdStr = BaseFields.id_required


class ResponseUpdateProduct(ResponseGetProduct):
    pass


class RequestUpdateProduct(AllOptional):
    class Config:
        use_enum_values = True


class ProductForOrder(BaseModel):
    id: ObjectIdStr = BaseFields.id_required
    barcode: str = BaseFields.barcode_required
    product_code: str = BaseFields.product_code_required
    title: str = BaseFields.title_required
    cook_sign: CookRoles = BaseFields.cook_sign_required
    price: float = BaseFields.price_required

    class Config:
        use_enum_values = True


class ResponseGetProduct(AllRequired):
    id: ObjectIdStr = BaseFields.id_required

    class Config:
        use_enum_values = True
        orm_mode = True


class ResponseGetProducts(AllOptional):
    id: Optional[ObjectIdStr] = BaseFields.id

    class Config:
        use_enum_values = True
        orm_mode = True


class ListOfProducts(PaginatedResult):
    result: List[ResponseGetProducts]
