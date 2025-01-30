from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean
from sqlalchemy.sql import func
from ..database import Base

class Banheiro(Base):
    __tablename__ = "banheiros"
    
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=False)
    accessibility = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())