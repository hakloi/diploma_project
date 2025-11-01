from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# относится к разряду
# ORM - object relational mapping
# работаем с объектами библиотеки 
# sqlalchemy, работаем с бд но не
# используем sql

engine = create_engine("sqlite://./webml.db")

# функция для создания сессий
# сессия - последовательность запросов к СУБД
SessionLocal = sessionmaker(engine)