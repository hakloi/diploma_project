from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy import mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Topic(Base):
    __tablename__ = "topics"
    
    id : Mapped[int] = mapped_column(primary_key=True) 
    title : Mapped[str] = mapped_column(index=True) 
    content : Mapped[str] = mapped_column()
    
class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(index=True)
    hashed_password : Mapped[str] = mapped_column()
    email : Mapped[str] = mapped_column(index=True)
    created_at : Mapped[datetime] = mapped_column()
    last_login : Mapped[datetime] = mapped_column()
    is_active : Mapped[bool] = mapped_column(default=True)
    is_online : Mapped[bool] = mapped_column(default=False)
    
    # для персонализации и прогресса
    skill_level : Mapped[str] = mapped_column()
    preferred_topics : Mapped[str] = mapped_column()
    learning_goals : Mapped[str] = mapped_column()
    completed_topics : Mapped[str] = mapped_column()
    total_progress : Mapped[int] = mapped_column(default=0)
    current_topic_id : Mapped[int] = mapped_column()
    streak_days : Mapped[int] = mapped_column(default=0)
    