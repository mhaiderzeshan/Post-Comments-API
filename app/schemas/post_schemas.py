from pydantic import BaseModel
from typing import Optional



class PostBase(BaseModel):
    title: str
    content: str
    user_id: int


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostResponse(PostBase):
    post_id: int
    user_id: int

    class Config:
        from_attributes = True