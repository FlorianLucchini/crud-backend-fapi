from sqlalchemy import Column, Integer, String, Boolean
from ..database.database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(String)
    birthday = Column(String)
    gender = Column(String)
    country = Column(String)
    phone_number = Column(String)

