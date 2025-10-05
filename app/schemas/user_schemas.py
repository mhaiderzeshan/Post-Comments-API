from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True
