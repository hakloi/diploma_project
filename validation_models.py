from typing import Annotated

from pydantic import Field, BaseModel, ConfigDict

IdType = Annotated[int, Field(gt=0)]
NameType = Annotated[str, Field(min_length=2, max_length=100)]
DescriptionType = Annotated[str, Field(min_length=5, max_length=100)]
TopicType = Annotated[str, Field(min_length=2, max_length=50)]

# базовый класс курса
class CourseBase(BaseModel):
    name: NameType
    description: DescriptionType

# параметры важные для создания курса
class CourseCreate(CourseBase):
    topic: TopicType
    rating: float = Field(ge=0, le=5)

# параметры которые будут выходить при чтении
class CourseOut(CourseBase):
    model_config = ConfigDict(from_attributes=True)

    course_id: IdType
    topic: str
    rating: float
    owner_id: int

# параметры для изменения курса
class CourseUpdate(BaseModel):
    name: NameType | None = None
    description: DescriptionType | None = None
    rating: float | None = Field(default=None, ge=0, le=5)
