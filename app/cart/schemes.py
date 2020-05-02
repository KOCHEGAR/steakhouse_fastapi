
from pydantic import BaseModel, Field


class ResponseCreateCart(BaseModel):
    id: str = Field(..., title='ID корзины')
    total_count: int = Field(..., title='Общее количство товара в корзине')
    total_price: float = Field(..., title='Цена за всё в корзине')
    # ordered_products =
