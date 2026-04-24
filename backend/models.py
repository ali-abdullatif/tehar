from sqlalchemy import Column, Integer, String, Text, Float
from database import Base

class JewelryItem(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(Text, nullable=True)
    price = Column(Float)
    image_url = Column(String(500), nullable=True)
