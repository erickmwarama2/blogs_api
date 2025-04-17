from enum import Enum
from typing import Optional
from fastapi import FastAPI, status, Response

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello world'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}

@app.get(
    '/blog/all',
    tags=['blog'],
    summary='Retrieve all blogs',
    description='This API call simulates retrieving of fetching all blogs',
    response_description='A list of all blogs'
    )
def get_all_blogs(page=1, page_size: Optional[int] = 20):
    return {'message': f'All {page_size} blogs on page {page}'}

class BlogType(str, Enum):
    short= 'short'
    story= 'story'
    howto= 'howto'

@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}

    response.status_code = status.HTTP_200_OK
    return {'message': f'Blog with id {id}'}

@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comments'])
def get_blog_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str]=None):
    '''
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    '''
    return {'blog_id': id, 'comment_id': comment_id, 'valid': valid, 'username': username}
