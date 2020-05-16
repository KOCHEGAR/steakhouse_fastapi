from typing import Optional, List

from pydantic import BaseModel, Field

from app.subtypes.schemes import ResponseGetSubtype
from app.utils.custom_types import ObjectIdStr
from app.utils.pagination import PaginatedResult


class BaseFields:
    id: ObjectIdStr = Field(title='ID of type')
    id_required: ObjectIdStr = Field(..., title='ID of type')
    title: str = Field(title='Title of type')
    title_required: str = Field(..., title='Title of type')
    status: bool = Field(title='Active type or not')
    status_required: bool = Field(..., title='Active type or not')
    is_promo: bool = Field(title='Is it promo?')
    is_promo_required: bool = Field(..., title='Is it promo?')
    subtypes: List[ResponseGetSubtype] = Field(title='list of subtypes')
    subtypes_required: List[ResponseGetSubtype] = Field(..., title='list of subtypes')


class AllRequired(BaseModel):
    title: str = BaseFields.title_required
    status: bool = BaseFields.status_required
    is_promo: bool = BaseFields.is_promo_required


class AllOptional(BaseModel):
    title: Optional[str] = BaseFields.title
    status: Optional[bool] = BaseFields.status
    is_promo: Optional[bool] = BaseFields.is_promo


class RequestCreateType(AllRequired):
    pass


class ResponseCreateType(AllRequired):
    id: ObjectIdStr = BaseFields.id_required

    class Config:
        orm_mode = True


class ResponseGetType(AllRequired):
    id: ObjectIdStr = BaseFields.id_required

    class Config:
        orm_mode = True


class ResponseGetTypes(AllOptional):
    id: ObjectIdStr = BaseFields.id_required

    class Config:
        orm_mode = True


class RequestUpdateType(AllOptional):
    pass


class ListOfTypes(PaginatedResult):
    result: List[ResponseGetTypes]


class ResponseGetTypeSubtypes(BaseModel):
    subtypes: List[ResponseGetSubtype] = BaseFields.subtypes_required

    class Config:
        orm_mode = True
