# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from ..database import Base 

# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, nullable=False, index=True)
#     hashed_password = Column(String, nullable=False)
#     name = Column(String, nullable=False)
#     learning_progress = Column(Integer, nullable=False, default=0)
 
#     def __repr__(self):
#         return f"User(id={self.id}, email={self.email}, hashed_password={self.hashed_password})"
