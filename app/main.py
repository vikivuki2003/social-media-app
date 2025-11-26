from hmac import new
from poplib import CR
from fastapi import FastAPI
from fastapi.params import Body
from random import randrange

from sqlalchemy.orm import Session, query
from . import models
from .database import engine
from .routers import post, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

my_posts = [{"title": "My first post", "content": "Content in my post", "id": 1}, {"title":
"favorite foods", "content": " I like pizza", "id": 2}]

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return "Hello"