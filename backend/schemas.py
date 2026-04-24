from pydantic import BaseModel
from typing import Optional, List

# Category Schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

# Item Schemas
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category_id: Optional[int] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    category: Optional[Category] = None

    class Config:
        from_attributes = True
