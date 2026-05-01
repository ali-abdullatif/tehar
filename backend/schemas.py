from pydantic import BaseModel
from typing import Optional, List

class ConfigUpdate(BaseModel):
    key: str
    value: str

class Config(ConfigUpdate):
    class Config:
        from_attributes = True

# Tracking Schemas
class EventCreate(BaseModel):
    event_type: str
    product_id: Optional[int] = None
    quantity: Optional[int] = 1
    session_id: str
    metadata_json: Optional[str] = "{}"

# Analytics Schemas
class DailyStats(BaseModel):
    date: str
    count: int

class HourlyStats(BaseModel):
    hour: int
    count: int

class ProductStats(BaseModel):
    product_name: str
    count: int

class AnalyticsDashboard(BaseModel):
    daily_sales: List[DailyStats]
    hourly_activity: List[HourlyStats]
    top_viewed: List[ProductStats]
    top_cart: List[ProductStats]
    conversion_funnel: dict
    cart_abandonment_rate: float

# Category Schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

# Image Schemas
class ItemImageBase(BaseModel):
    url: str

class ItemImageCreate(ItemImageBase):
    pass

class ItemImage(ItemImageBase):
    id: int
    item_id: int

    class Config:
        from_attributes = True

# Item Schemas
class ItemBase(BaseModel):
    product_code: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category_id: Optional[int] = None

class ItemCreate(ItemBase):
    gallery_images: Optional[List[str]] = [] # List of URLs

class Item(ItemBase):
    id: int
    category: Optional[Category] = None
    images: List[ItemImage] = []

    class Config:
        from_attributes = True
