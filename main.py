from fastapi import FastAPI
from modules.users.routes import createUser, readUser, updateUser, deleteUser

app = FastAPI(
    title="Tugas 2: User CRUD API",
    description="API untuk mengelola data user dengan validasi dan otorisasi sederhana.",
    version="1.0.0"
)

# Menggabungkan semua router dari modul users
app.include_router(createUser.router, tags=["Users"])
app.include_router(readUser.router, tags=["Users"])
app.include_router(updateUser.router, tags=["Users"])
app.include_router(deleteUser.router, tags=["Users"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the User CRUD API!"}

# Membersihkan database (hanya untuk keperluan testing)
@app.on_event("startup")
def startup_event():
    createUser.db.clear()