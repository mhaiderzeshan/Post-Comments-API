from sqlalchemy.orm import Session
from typing import Optional
from app import models
from app.schemas import post_schemas


def create_post(db: Session, post: post_schemas.PostCreate):
    db_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session):
    return db.query(models.Post)


def get_post_by_id(db: Session, post_id: int) -> Optional[models.Post]:
    return db.query(models.Post).filter(models.Post.post_id == post_id).first()


def update_post(id: int, db: Session, post: post_schemas.PostUpdate):
    db_post = db.query(models.Post).filter(models.Post.post_id == id).first()
    if db_post:
        if post.title is not None:
            setattr(db_post, "title", post.title)
        if post.content is not None:
            setattr(db_post, "content", post.content)
        db.commit()
        db.refresh(db_post)
    return db_post


def delete_post(id: int, db: Session):
    db_post = db.query(models.Post).filter(models.Post.post_id == id).first()

    if not db_post:
        return None

    db.delete(db_post)
    db.commit()

    return db_post
