from fastapi import FastAPI

from database import SessionLocal

app = FastAPI()

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# database - courses
@app.get("/")
def greet():
    return "Hello World"

@app.get("/api/courses/")
def get_all_courses():
    return

@app.get("/api/courses/{course_id}")
def get_course_by_id(course_id: int):
    return

@app.post("/api/courses/")
def create_course():
    return

@app.patch("/api/courses/{course_id}")
def update_course_by_id(course_id: int):
    return

@app.delete("/api/courses/{course_id}")
def delete_course_by_id(course_id: int):
    return

# users