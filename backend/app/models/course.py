from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base 

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category_id = Column(Integer, nullable=False)
    lessons_amount = Column(Integer, nullable=False)
    
    category = relationship("Category", back_populates="courses")
    
    # для правильного вывода 
    def __repr__(self):
        return f"Course(id={self.id}, name={self.name}, description={self.description}, category_id={self.category_id})"