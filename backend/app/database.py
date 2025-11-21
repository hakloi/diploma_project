from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
)

# постоянно делает сессии на соединение с бд
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# базовый класс для всех моделей
Base = declarative_base()

# вызывает новую сессиб кд когда нужно соед к бд
def get_db():
    db = SessionLocal()
    try:
        # попытка пеердать сессию
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)