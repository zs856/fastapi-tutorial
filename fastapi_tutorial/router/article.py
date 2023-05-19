from typing import List
from fastapi import APIRouter, Depends
from schemas import UserBase
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_user
from schemas import UserDisplay
from schemas import ArticleDisplay
from db import db_article
from schemas import ArticleBase
router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create article
@router.post('/',response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db,request)
# Get specific article
@router.get('/{id}',response_model=ArticleDisplay)
def  get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)