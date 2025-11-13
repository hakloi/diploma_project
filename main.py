from fastapi import FastAPI
from routers import user

app = FastAPI(title="MLLab API", description="ML Educational Platform")

# routers
app.include_router(user.router)

@app.get("/")
def home_page():
    return {"message": "Welcome to MLLab!"}