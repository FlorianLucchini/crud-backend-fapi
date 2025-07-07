from pydantic import BaseModel
from datetime import date, datetime

class UserBase(BaseModel):
    username: str
    email: str
    birthday: date | None = None
    gender: str | None = None
    country: str | None = None
    phoner_number: str | None = None
    
class UserCreate(UserBase):
    password: str
    
class UserUpdate(UserBase):
    password: str | None = None
    email: str | None = None
    username: str | None = None
    birthday: date | None = None
    gender: str | None = None
    country: str | None = None
    phone_number: str | None = None
    
class User(UserBase):
    id: int
    created_at: datetime | None = None
    
    class Config:
        from_attributes = True
