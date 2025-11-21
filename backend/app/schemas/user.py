from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    name: str = Field(..., min_length=1, max_length=100)
    
    # ML персонализация - начальные предпочтения
    learning_style: str = Field(default="visual", pattern="^(visual|auditory|kinesthetic)$")
    preferred_difficulty: str = Field(default="medium", pattern="^(easy|medium|hard)$")
    learning_pace: str = Field(default="normal", pattern="^(slow|normal|fast)$")

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    name: str
    created_at: datetime
    last_login: Optional[datetime]
    is_active: bool
    
    # ML данные для персонализации
    learning_style: str
    preferred_difficulty: str
    learning_pace: str
    active_hours: List[int] = Field(default_factory=list, description="Hours when user is most active")
    session_duration_avg: int = Field(default=0, description="Average session duration in minutes")
    
    # Предпочтения и прогресс
    preferred_categories: List[int] = Field(default_factory=list)
    enrolled_courses: List[int] = Field(default_factory=list)
    completed_courses: List[int] = Field(default_factory=list)
    completion_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    streak_days: int = Field(default=0, ge=0)
    total_study_time: int = Field(default=0, description="Total study time in minutes")
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    learning_style: Optional[str] = Field(None, pattern="^(visual|auditory|kinesthetic)$")
    preferred_difficulty: Optional[str] = Field(None, pattern="^(easy|medium|hard)$")
    learning_pace: Optional[str] = Field(None, pattern="^(slow|normal|fast)$")
    preferred_categories: Optional[List[int]] = None

class UserCourseInteraction(BaseModel):
    user_id: int
    course_id: int
    interaction_type: str = Field(..., pattern="^(view|start|complete|rate|bookmark|pause)$")
    duration_seconds: int = Field(default=0, ge=0)
    progress_percent: int = Field(default=0, ge=0, le=100)
    rating: Optional[int] = Field(None, ge=1, le=5)
    timestamp: datetime = Field(default_factory=datetime.now)
    
class UserLearningAnalytics(BaseModel):
    user_id: int
    recommended_courses: List[int] = Field(default_factory=list)
    learning_path: List[int] = Field(default_factory=list, description="Suggested course sequence")
    next_session_time: Optional[datetime] = None
    difficulty_adjustment: str = Field(default="maintain", pattern="^(increase|decrease|maintain)$")