from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    # ... - это значит что параметр обязательный
    name: str = Field(
        ..., 
        min_length=2,
        max_length=50,
        description="Category name" #используется в placeholder 
        )
    
    description: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Category description"
        )
    
    image_url: Optional[str] = Field(
        None,
        description="Category image URL"
        )
    
# просто наследуем
class CategoryCreate(CategoryBase):
    pass

# тут будет еще айди, так как мы хотим получать инфу по категории
# + другие параметры подтянутся
class CategoryResponse(CategoryBase):
    id: int = Field(
        ...,
        description="Unique category id"
        )
    
    class Config:
        from_attributes = True