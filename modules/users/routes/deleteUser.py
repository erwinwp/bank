from fastapi import APIRouter, HTTPException, Header, status
from uuid import UUID

from modules.users.routes.createUser import db
from modules.users.schema.schemas import UserRole
from modules.users.routes.readUser import find_user_by_id

router = APIRouter()

@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: UUID, x_user_role: str = Header(...)):
    """
    Menghapus data user.
    - Hanya bisa diakses oleh ADMIN.
    """
    if x_user_role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Forbidden: Admins only")
        
    user = find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    db.remove(user)
    return {"message": f"User {user_id} deleted successfully"}