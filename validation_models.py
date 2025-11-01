from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional
from datetime import datetime

# Topic types
TitleType = Annotated[str, Field(min_length=1, max_length=100)]
ContentType = Annotated[str, Field(min_length=1, max_length=1000)]

# User types
UsernameType = Annotated[str, Field(min_length=3, max_length=50)]
PasswordType = Annotated[str, Field(min_length=6, max_length=100)]
SkillLevelType = Annotated[str, Field(pattern="^(beginner|intermediate|advanced)$")]
ProgressType = Annotated[int, Field(ge=0, le=100)]
StreakType = Annotated[int, Field(ge=0)]

class TopicBase(BaseModel):
    title: TitleType
    content: ContentType
    
class UserCreate(BaseModel):
    username: UsernameType
    email: EmailStr
    password: PasswordType
    skill_level: SkillLevelType = "beginner"
        
class UserResponse(BaseModel):
    id: int
    username: UsernameType
    email: EmailStr
    created_at: datetime
    last_login: Optional[datetime]
    is_active: bool
    is_online: bool
    skill_level: SkillLevelType
    preferred_topics: Optional[str]
    learning_goals: Optional[str]
    completed_topics: Optional[str]
    total_progress: ProgressType
    current_topic_id: Optional[int]
    streak_days: StreakType
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    skill_level: Optional[SkillLevelType] = None
    preferred_topics: Optional[str] = None
    learning_goals: Optional[str] = None