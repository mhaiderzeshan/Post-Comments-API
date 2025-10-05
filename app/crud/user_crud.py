from sqlalchemy.orm import Session
from typing import Optional
from app import models
from app.schemas import user_schemas


def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return db.query(models.User)
