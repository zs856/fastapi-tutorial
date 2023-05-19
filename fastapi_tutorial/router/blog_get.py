from enum import Enum
from typing import Optional
from fastapi import APIRouter, Depends,status, Response

from .blog_post import required_functionality
router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get("/hello")
def index():
    return {"message": "Hello World"}


# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}
@router.get(
    "/all",
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs",
    response_description='The list of available blogs'
)
def get_blogs(page=1, page_size: Optional[int]=None,req_parameter: dict = Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}",'req':req_parameter}


@router.get("/{id}/comments/{comment_id}")
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None,req_parameter: dict = Depends(required_functionality)
):
    """
    Simulates retrieving a comment of a blog

    - **id (int)**: mandatory path parameter
    - **comment_id (int)**: mandatory path parameter
    - **valid (bool, optional)**: optional query parameter. Defaults to True.
    - **username (Optional[str], optional)**: optional query parameter. Defaults to None.
    """
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}
