from typing import Optional
from fastapi import FastAPI
from routers import blog_get

app = FastAPI()
app.include_router(blog_get.router);

@app.get('/hello')
def index():
    return {'message': 'Hello world'}