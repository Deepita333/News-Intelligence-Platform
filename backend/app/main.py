from fastapi import FastAPI
from app.api import articles

app = FastAPI()

app.include_router(
    articles.router,
    prefix="/articles"
)

@app.get("/")
def root():
    return {"message": "News Intelligence Platform API is running!"}