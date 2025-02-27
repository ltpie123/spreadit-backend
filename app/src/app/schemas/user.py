from datetime import datetime
from pydantic import BaseModel, const, EmailStr


class UserBase(BaseModel):
    username: const(min_length=3, max_length=30, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr


class UserCreate(UserBase):
    password: const(min_length=8, max_length=64)


# TODO: Add more fields
