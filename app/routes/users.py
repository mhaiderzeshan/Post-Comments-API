from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user_crud
from app.schemas import user_schemas
from app.database import get_db

router = APIRouter(prefix="/User", tags=["/User"])


@router.post("/create_user", response_model=user_schemas.UserBase)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    if user.email is None or user.password is None:
        raise HTTPException(status_code=400, detail="Email and password are required")
    db_user = user_crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


@router.post("/login", response_model=user_schemas.UserResponse)
def login(email: user_schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db=db, email=email.email)
    if db_user is None or db_user.password != email.password:  # type: ignore
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_user


@router.get("/", response_model=list[user_schemas.UserBase])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_users(db=db)
