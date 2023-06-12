from typing import List
from fastapi import APIRouter, Depends
from ..auth.oauth2 import get_current_user
from ..schemas import UserBase
from sqlalchemy.orm import Session
from ..auth.oauth2 import oauth2_scheme 
from ..db.database import get_db
from ..db import db_user
from ..schemas import UserDisplay
from ..schemas import ArticleDisplay
from ..db import db_article
from ..schemas import ArticleBase
router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create article
@router.post('/',response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: str= Depends(get_current_user)):
    return db_article.create_article(db,request)
# Get specific article
@router.get('/{id}')#,response_model=ArticleDisplay)
def  get_article(id: int, db: Session = Depends(get_db), current_user: str= Depends(get_current_user)):
    return {
        'data':db_article.get_article(db, id),
        'current_user':current_user
    } 