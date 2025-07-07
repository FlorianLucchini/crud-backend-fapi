from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from ..database.database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime)
    birthday = Column(Date)
    gender = Column(String)
    country = Column(String)
    phone_number = Column(String)

