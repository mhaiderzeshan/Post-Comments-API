from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models
from app.crud import comment_crud
from app.schemas import comment_schemas
from app.database import get_db

router = APIRouter(prefix="/Comment", tags=["/Comment"])


@router.post("/create_comment", response_model=comment_schemas.CommentBase)
def create_comment(comment: comment_schemas.CommentCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.user_id == comment.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {comment.user_id} does not exist"
        )

    post = db.query(models.Post).filter(
        models.Post.post_id == comment.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {comment.post_id} does not exist"
        )

    new_comment = comment_crud.create_comment(db=db, comment=comment)
    return new_comment


@router.get("/posts/{id}/comments", response_model=list[comment_schemas.CommentResponse])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.post_id == post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with the id {post_id} does not exist"
        )

    comments = comment_crud.get_comments_by_post(db=db, post_id=post_id)

    if not comments:
        raise HTTPException(
            status_code=404,
            detail=f"No comments found for post {post_id}"
        )

    return comments


@router.delete("/comments/{id}", response_model=comment_schemas.CommentResponse)
def delete_comment(id: int, db: Session = Depends(get_db)):
    db_comment = comment_crud.delete_comment(db=db, id=id)

    if not db_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment with ID {id} does not exist"
        )

    return db_comment
