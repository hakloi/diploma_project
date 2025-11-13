from fastapi import FastAPI
from routers import user
import uvicorn


def create_app():
    app = FastAPI(title="MLLab API", description="ML Educational Platform")

    # routers
    app.include_router(user.router)

    @app.get("/")
    def home_page():
        return {"message": "Welcome to MLLab!"}
    
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  
        reload=True
    )