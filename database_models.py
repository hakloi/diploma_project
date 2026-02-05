import enum
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped

class Base(DeclarativeBase):
    pass

class Status(enum.Enum):
    PROGRESS = 'In Progress'
    NOT_STARTED = 'Not Started'
    COMPLETED = 'Completed'

class Course(Base):
    __tablename__ = "courses"

    course_id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(100), nullable=False)
    description: Mapped[str] = Column(String(100), nullable=False)
    topic: Mapped[str] = Column(String(50), nullable=False)
    rating: Mapped[float] = Column(Float, default=0)

    # owner_id: Mapped[int] = Column(
    #     Integer,
    #     ForeignKey("users.id"),
    #     nullable=False
    # )

