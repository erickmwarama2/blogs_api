from typing import List, Optional
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"message": "OK", "data": blog, "id": id, "version": version}

@router.post('/new/{id}/comment')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_id: int = Query(
        None,
        title='Id of the comment',
        description='Some description for the comment id',
        alias='commentId'
        ),
    comment: str = Body(...),
    v: Optional[List[str]] = Query(None)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'comment': comment,
        'v': v
    }