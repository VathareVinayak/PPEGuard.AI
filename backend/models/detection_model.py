from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)
    category = Column(String, nullable=False)  # 'wearing' or 'not_wearing'
    detected_items = Column(String, nullable=False)  # e.g., 'Mask, NO-Hardhat'
    timestamp = Column(DateTime, default=datetime.utcnow)
