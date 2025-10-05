from fastapi import FastAPI
from app.routes import users, posts, comments
from app.database import Base, engine
app = FastAPI(title="Post & Comments API")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Welcome"}
