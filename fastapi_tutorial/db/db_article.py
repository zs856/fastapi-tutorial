from fastapi import HTTPException, status

from exception import StoryException
from .models import DbArticle
from sqlalchemy.orm.session import Session
from schemas import ArticleBase
def create_article(db:Session, request: ArticleBase):
    if request.content.startswith('Once upon a time'):
        raise StoryException('No sotries please')
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published = request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
def get_article(db: Session, id:int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {id} not found')
    return article