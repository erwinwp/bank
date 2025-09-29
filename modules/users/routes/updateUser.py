from fastapi import APIRouter, HTTPException, Header
from uuid import UUID
from datetime import datetime

from modules.users.routes.createUser import db
from modules.users.schema.schemas import User, UserCreate, UserRole
from modules.users.routes.readUser import find_user_by_id

router = APIRouter()

@router.put("/users/{user_id}", response_model=User)
def update_user(
    user_id: UUID, 
    user_update: UserCreate, 
    x_user_role: str = Header(...)
):
    """
    Memperbarui data user.
    - Hanya bisa diakses oleh ADMIN.
    """
    if x_user_role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Forbidden: Admins only")

    user = find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update data
    user.username = user_update.username
    user.email = user_update.email
    user.role = user_update.role
    user.updated_at = datetime.utcnow()
    
    return user