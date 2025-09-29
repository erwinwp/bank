from fastapi import APIRouter, HTTPException, Header, Depends
from typing import List, Optional
from uuid import UUID

from modules.users.routes.createUser import db # Mengimpor 'db' dari createUser
from modules.users.schema.schemas import User, UserRole

router = APIRouter()

# Helper function untuk mencari user
def find_user_by_id(user_id: UUID) -> Optional[User]:
    for user in db:
        if user.id == user_id:
            return user
    return None

@router.get("/users/", response_model=List[User])
def get_all_users(x_user_role: str = Header(...)):
    """
    Mendapatkan semua data user.
    - Hanya bisa diakses oleh ADMIN.
    """
    if x_user_role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Forbidden: Admins only")
    return db

@router.get("/users/{user_id}", response_model=User)
def get_user_by_id(
    user_id: UUID, 
    x_user_id: str = Header(...), 
    x_user_role: str = Header(...)
):
    """
    Mendapatkan data user berdasarkan ID.
    - ADMIN bisa mengakses data user manapun.
    - STAFF hanya bisa mengakses datanya sendiri.
    """
    user = find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Otorisasi
    if x_user_role == UserRole.STAFF and str(user.id) != x_user_id:
        raise HTTPException(status_code=403, detail="Forbidden: You can only view your own data")
        
    return user