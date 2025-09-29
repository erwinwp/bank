from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID
from datetime import datetime

from modules.users.schema.schemas import User, UserCreate

# List untuk menyimpan data user di memori
db: List[User] = []

router = APIRouter()

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate):
    """
    Membuat user baru.
    - Username dan Email harus unik.
    """
    # Cek duplikasi username atau email
    for existing_user in db:
        if existing_user.username == user_in.username:
            raise HTTPException(status_code=400, detail="Username already registered")
        if existing_user.email == user_in.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    # Membuat objek User lengkap dari input UserCreate
    # (Password tidak disimpan atau dikembalikan setelah pembuatan)
    new_user = User(
        username=user_in.username,
        email=user_in.email,
        role=user_in.role,
        # Di dunia nyata, password akan di-hash sebelum disimpan
    )
    db.append(new_user)
    return new_user