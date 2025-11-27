from hmac import new
from poplib import CR
from fastapi import FastAPI
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from sqlalchemy.orm import Session, query
from . import models
from .database import engine
from .routers import post, user, auth

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Vorza2003_', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was succesfull')
        break
    except Exception as error:
        print("Connecting to database was failed")
        print("Error:", error)
        time.sleep(2)



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
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello"}