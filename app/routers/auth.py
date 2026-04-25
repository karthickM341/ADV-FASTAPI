from fastapi import APIRouter, HTTPException
from app.schemas.auth import Login
from app.core.security import create_token

router = APIRouter()

fake_user = {"username": "admin", "password": "admin"}

@router.post("/login")
def login(user: Login):
    if user.username != fake_user["username"] or user.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": user.username})
    return {"access_token": token}