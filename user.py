from fastapi import APIRouter, HTTPException
from app.database import users_collection
from app.models import User

router = APIRouter()

@router.post("/register")
def register(user: User):
    users_collection.insert_one({
        "email": user.email,
        "password": user.password
    })
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User):
    db_user = users_collection.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email")

    if db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}
