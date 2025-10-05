from sqlalchemy.orm import Session
from typing import Optional
from app import models
from app.schemas import comment_schemas


def create_comment(db: Session, comment: comment_schemas.CommentCreate):
    db_comment = models.Comment(
        content=comment.content,
        post_id=comment.post_id,
        user_id=comment.user_id
    )

    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)

    return db_comment


def get_comments_by_post(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()


def delete_comment(db: Session, id: int):
    comment = db.query(models.Comment).filter(
        models.Comment.comment_id == id).first()

    if not comment:
        return None

    db.delete(comment)
    db.commit()
    return comment
