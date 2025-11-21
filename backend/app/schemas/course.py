from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from category import CategoryResponse

class CourseBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Course name")
    description: str = Field(..., min_length=1, max_length=1000, description="Course description")
    author: str = Field(..., min_length=1, max_length=100, description="Course author")
    category_id: int = Field(..., description="Category ID")
    image_url: Optional[str] = Field(None, description="Course image URL")

class CourseCreate(CourseBase):
    difficulty_level: str = Field(default="beginner", pattern="^(beginner|intermediate|advanced)$")
    estimated_hours: int = Field(default=10, ge=1, le=1000, description="Estimated completion time in hours")

class CourseUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, min_length=1, max_length=1000)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    difficulty_level: Optional[str] = Field(None, pattern="^(beginner|intermediate|advanced)$")
    estimated_hours: Optional[int] = Field(None, ge=1, le=1000)

class CourseResponse(CourseBase):
    id: int
    difficulty_level: str
    estimated_hours: int
    created_at: datetime
    updated_at: Optional[datetime]
    is_active: bool
    total_enrollments: int = Field(default=0)
    category: CategoryResponse = Field(..., description="Category details")
    
    class Config:
        from_attributes = True
        
class CourseListResponse(BaseModel):
    courses: list[CourseResponse]
    total: int

    
