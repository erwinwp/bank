import re
from uuid import UUID, uuid4
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime

class UserRole(str, Enum):
    """
    Enumerasi untuk peran pengguna.
    """
    ADMIN = "admin"
    STAFF = "staff"

class UserBase(BaseModel):
    username: str = Field(..., min_length=6, max_length=15, pattern=r"^[a-z0-9]+$")
    email: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    role: UserRole = Field(..., description="Peran pengguna: admin atau staff")

    @validator('username')
    def username_alphanumeric_lowercase(cls, v):
        if not v.islower():
            raise ValueError('Username must be all lowercase')
        return v

class UserCreate(UserBase):
    """
    Skema untuk membuat user baru, memerlukan password.
    """
    password: str = Field(..., min_length=8, max_length=20)

    @validator('password')
    def password_complexity(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r"[a-z]", v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r"[0-9]", v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r"[!@]", v):
            raise ValueError('Password must contain at least one of the special characters: !@')
        if re.search(r"[^a-zA-Z0-9!@]", v):
            raise ValueError('Password contains invalid characters')
        return v

class User(UserBase):
    """
    Skema untuk menampilkan data user, termasuk field yang auto-generated.
    """
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True # Memungkinkan mapping langsung dari model data lain