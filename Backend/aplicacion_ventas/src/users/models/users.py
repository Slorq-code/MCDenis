from datetime import datetime

import bcrypt
from sqlalchemy import Boolean, Column, DateTime, Integer, String

from general.ormbase import Base


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


class User(Base):
    """User model"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(45), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, username: str, password: str, is_superuser: bool = False):
        self.username = username  # type: ignore
        self.hashed_password = get_password_hash(password)  # type: ignore
        self.is_superuser = is_superuser  # type: ignore

    def check_password(self, password: str) -> bool:
        """Check the password against the hashed password stored in the database"""
        return verify_password(password, str(self.hashed_password))

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def display_name(self) -> str:
        return str(self.username)
