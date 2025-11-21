from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base 

class Category(Base):
    __tablename__ = "categories"
    
    # index - ускоряет поиск, так как индексирует параметр 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False)
    
    courses = relationship("Course", back_populates="category")
    
    # repr - в админке можно вывести и показывается в удобном формате 
    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, description={self.description})"
    