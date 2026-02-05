from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from database_models import Course
from validation_models import CourseOut, CourseCreate

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

@app.get("/api/courses/{start}/{limit}", response_model=list[CourseOut])
def get_all_courses_scroll(start: int, limit: int, session: Session = Depends(get_session)):
    return session.query(Course).offset(start).limit(limit).all()

@app.get("/api/courses/{course_id}", response_model=CourseOut)
def get_course_by_id(course_id: int, session: Session = Depends(get_session)):
    db_course = session.query(Course).filter_by(id=course_id).first()

    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    return db_course

@app.post("/api/courses/", response_model=CourseOut)
def create_course(
        course: CourseCreate,
        session: Session = Depends(get_session)
):
    db_course = Course(
        name=course.name,
        description=course.description,
        topic=course.topic
    )
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course

@app.patch("/api/courses/{course_id}")
def update_course_by_id(course_id: int,
                        validation_course: CourseCreate,
                        session: Session = Depends(get_session)):
    course = session.query(Course).filter_by(id=course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    course.name = validation_course.name
    course.description = validation_course.description
    course.topic = validation_course.topic

    session.commit()
    return {}


@app.delete("/api/courses/{course_id}")
def delete_course_by_id(course_id: int, session: Session = Depends(get_session)):
    db_course = session.query(Course).filter_by(id=course_id).first()

    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    session.delete(db_course)
    session.commit()
    return {"message": "Course deleted successfully"}

# users