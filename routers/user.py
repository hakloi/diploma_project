from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate
from services.user_service import users

router = APIRouter(
    prefix="/users",  
    tags=["users"]   
)

@router.get("/me")
def read_user_me():
    return {"user_id": "the current user"}

@router.get("/")
def get_all_users():
    return {"users": list(users.values())}

@router.get("/{user_id}")
def read_user(user_id: int):
    if user_id in users:
        return users[user_id]
    return {"error": "User not found"}

@router.post("/")
def create_user(user: UserCreate):
    for existing_user in users.values():
        if existing_user["username"] == user.username:
            raise HTTPException(400, detail="User with this username already exists!")

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {
        "user_id": new_id,
        "username": user.username,
        "email": user.email,
        "password_hash": user.password_hash
    }
    return {"message": "User created successfully", "user": users[new_id]}