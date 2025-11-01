from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class Topics(str, Enum):
    math = "math"
    ml = "ml"
    ai = "ai"
    cv = "cv"
    nlp = "nlp"
    python = "python"
    alg = "alg"

@app.get("/")
def home_page():
    return {"message": "Hello, friend!"}

@app.get("/topics/{topic_title}")
def read_item(topic_title: Topics):
    if topic_title == Topics.math:
        return {"topic_title": topic_title,
                "message": "It will be the best adventure to numbers!"}
    if topic_title == Topics.ml:
        return {"topic_title": topic_title,
                "message": "Classic ML!"}
        
    return {"topic_title": topic_title,
            "message": "You chose the right one!"}

@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}

