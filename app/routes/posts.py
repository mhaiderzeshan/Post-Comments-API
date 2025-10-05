from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import post_crud
from app.schemas import post_schemas
from app.database import get_db

router = APIRouter(prefix="/Post", tags=["/Post"])


@router.post("/create_post", response_model=post_schemas.PostBase)
def create_post(post: post_schemas.PostCreate, db: Session = Depends(get_db)):
    return post_crud.create_post(db=db, post=post)


@router.get("/posts", response_model=list[post_schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return post_crud.get_posts(db=db)


@router.get("/{post_id}", response_model=post_schemas.PostResponse)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return post_crud.get_post_by_id(db=db, post_id=post_id)


@router.put("/update_post/{post_id}", response_model=post_schemas.PostResponse)
def update_post(id: int, post: post_schemas.PostUpdate, db: Session = Depends(get_db)):
    db_post = post_crud.update_post(id=id, db=db, post=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.delete("/delete_post/{post_id}", response_model=post_schemas.PostResponse)
def delete_post(id: int, db: Session = Depends(get_db)):
    db_post = post_crud.delete_post(db=db, id=id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return db_post

