# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from datetime import datetime

# class UserCreate(BaseModel):
#     """Create user"""
#     username: str
#     email: EmailStr
#     password: str  
#     skill_level: str = "beginner"

# class UserResponse(BaseModel):
#     """Get information about user, only needed info without security leak"""
#     user_id: int
#     username: str
#     email: str
#     created_at: datetime
#     last_login: Optional[datetime]
#     is_active: bool
#     is_online: bool
#     skill_level: str
#     preferred_topics: Optional[str]
#     learning_goals: Optional[str]
#     completed_topics: Optional[str]
#     total_progress: int
#     current_topic_id: Optional[int]
#     streak_days: int
    
#     class Config:
#         from_attributes = True

# class UserUpdate(BaseModel):
#     """Update info about user, only fields that can be updated"""
#     username: Optional[str] = None
#     email: Optional[EmailStr] = None
#     password: Optional[str] = None
#     skill_level: Optional[str] = None
#     preferred_topics: Optional[str] = None
#     learning_goals: Optional[str] = None

