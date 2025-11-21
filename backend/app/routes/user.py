from fastapi import APIRouter, HTTPException
from datetime import datetime

from schemas.user import UserCreate, UserResponse, UserUpdate
from services.user_service import users

router = APIRouter(
    prefix="/users",  
    tags=["users"]   
)

# нужна аутентификация, заглушка, потом вернемся
"""Get current user information"""
@router.get("/me")
def read_user_me(current_user_id : int) -> UserResponse:
    if current_user_id in users:
        return UserResponse(**users[current_user_id])
    raise HTTPException(404, "User not found")

"""Get list of users"""
@router.get("/")
def get_all_users() -> list[UserResponse]:
    return [UserResponse(**user) for user in users.values()]

"""Get user information by its id"""
@router.get("/{user_id}")
def get_user_by_id(user_id: int) -> UserResponse:
    for user in users.values():
        if user["user_id"] == user_id:
            return UserResponse(**user)
    raise HTTPException(404, "User not found")

"""Create user"""
@router.post("/")
def create_user(user: UserCreate) -> UserResponse:
    for existing_user in users.values():
        if existing_user["username"] == user.username:
            raise HTTPException(400, detail="User with this username already exists!")

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {
        "user_id": new_id,
        "username": user.username,
        "email": user.email,
        "password_hash": user.password,
        # вернуться и прохэшироавть пароль
        # "password_hash": hash_password(user.password),  
        "created_at": datetime.now(),
        "last_login": None,
        "is_active": True,
        "is_online": False,
        "skill_level": user.skill_level,
        "preferred_topics": None,
        "learning_goals": None,
        "completed_topics": None,
        "total_progress": 0,
        "current_topic_id": None,
        "streak_days": 0
    }
    return UserResponse(**users[new_id])

"""Change user information by its id"""
@router.put("/{user_id}")
def change_user(user_id: int, user_data: UserUpdate) -> UserResponse:
    if user_id not in users:
        raise HTTPException(404, "User not found")
    
    user = users[user_id]
    
    # optional tests for email and username
    if user_data.username is not None and user_data.username not in users:
        user["username"] = user_data.username
    else:
        raise HTTPException(404, "User with this name already exists!")
    
    
    if user_data.email is not None and user_data.email not in users:
        user["email"] = user_data.email
    else:
        raise HTTPException(404, "User with this email already exists!")
    
    # update non-unique data
    if user_data.password is not None:
        user["password_hash"] = user_data.password  # хеширование
    if user_data.skill_level is not None:
        user["skill_level"] = user_data.skill_level
    if user_data.preferred_topics is not None:
        user["preferred_topics"] = user_data.preferred_topics
    if user_data.learning_goals is not None:
        user["learning_goals"] = user_data.learning_goals
    
    return UserResponse(**user)

"""Delete user by its id"""
@router.delete("/{user_id}")
def delete_user(user_id : int):
    if user_id not in users:
        raise HTTPException(404, "User not found")
    
    users.pop(user_id)