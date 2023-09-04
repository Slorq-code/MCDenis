from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from general.ormbase import Base


class Worker(Base):
    """User model"""

    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(90), nullable=False)
    code = Column(String(45), nullable=False)
    location = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=False)
    email = Column(String(90), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
