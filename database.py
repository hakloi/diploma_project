from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_models import Base

engine = create_engine('sqlite:///courses.db')

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)