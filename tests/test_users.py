import sys
import os
import pytest
from fastapi.testclient import TestClient

# Menambahkan path root proyek agar bisa mengimpor 'main'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from modules.users.routes.createUser import db

client = TestClient(app)

# Data untuk testing
admin_user_payload = {
    "username": "adminuser",
    "email": "admin@example.com",
    "password": "Password!1",
    "role": "admin"
}

staff_user_payload = {
    "username": "staffuser",
    "email": "staff@example.com",
    "password": "Password@2",
    "role": "staff"
}

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Dijalankan sebelum setiap test
    db.clear()
    yield
    # Dijalankan setelah setiap test
    db.clear()

def test_create_admin_user():
    response = client.post("/users/", json=admin_user_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == admin_user_payload["username"]
    assert "id" in data

def test_create_staff_user():
    response = client.post("/users/", json=staff_user_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == staff_user_payload["username"]
    
def test_create_user_bad_password():
    bad_payload = staff_user_payload.copy()
    bad_payload["password"] = "pass"
    response = client.post("/users/", json=bad_payload)
    assert response.status_code == 422 # Unprocessable Entity

def test_read_all_users_as_admin():
    client.post("/users/", json=admin_user_payload)
    client.post("/users/", json=staff_user_payload)
    
    headers = {"X-User-Role": "admin"}
    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_read_all_users_as_staff_forbidden():
    headers = {"X-User-Role": "staff"}
    response = client.get("/users/", headers=headers)
    assert response.status_code == 403

def test_read_own_user_as_staff():
    staff_res = client.post("/users/", json=staff_user_payload)
    staff_id = staff_res.json()["id"]

    headers = {"X-User-Role": "staff", "X-User-ID": staff_id}
    response = client.get(f"/users/{staff_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == staff_id

def test_read_other_user_as_staff_forbidden():
    admin_res = client.post("/users/", json=admin_user_payload)
    admin_id = admin_res.json()["id"]
    staff_res = client.post("/users/", json=staff_user_payload)
    staff_id = staff_res.json()["id"]

    headers = {"X-User-Role": "staff", "X-User-ID": staff_id}
    response = client.get(f"/users/{admin_id}", headers=headers)
    assert response.status_code == 403

def test_delete_user_as_admin():
    staff_res = client.post("/users/", json=staff_user_payload)
    staff_id = staff_res.json()["id"]

    headers = {"X-User-Role": "admin"}
    response = client.delete(f"/users/{staff_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == f"User {staff_id} deleted successfully"
    
    # Verifikasi user sudah tidak ada
    get_response = client.get(f"/users/{staff_id}", headers={"X-User-Role": "admin", "X-User-ID": "any"})
    assert get_response.status_code == 404