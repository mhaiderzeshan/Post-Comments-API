from pydantic import BaseModel


class CommentBase(BaseModel):
    content: str
    post_id: int
    user_id: int


class CommentCreate(CommentBase):
    pass


class CommentResponse(CommentBase):
    comment_id: int

    class Config:
        from_attributes = True
