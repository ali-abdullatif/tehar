from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ItemCategory(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    
    items = relationship("JewelryItem", back_populates="category")

class SiteConfig(Base):
    __tablename__ = "site_config"

    key = Column(String(100), primary_key=True)
    value = Column(Text)

class ItemImage(Base):
    __tablename__ = "item_images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500))
    item_id = Column(Integer, ForeignKey("items.id"))

    item = relationship("JewelryItem", back_populates="images")

class JewelryItem(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(Text, nullable=True)
    price = Column(Float)
    image_url = Column(String(500), nullable=True) # Primary thumbnail
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    category = relationship("ItemCategory", back_populates="items")
    images = relationship("ItemImage", back_populates="item", cascade="all, delete-orphan")
