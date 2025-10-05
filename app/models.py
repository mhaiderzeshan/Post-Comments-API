from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    # Relationships
    posts = relationship("Post", back_populates="author",
                         cascade="all, delete-orphan")
    comments = relationship(
        "Comment", back_populates="commenter", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # Relationships
    author = relationship("User", back_populates="posts")
    comments = relationship(
        "Comment", back_populates="post", cascade="all, delete-orphan")


class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.post_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # Relationships
    post = relationship("Post", back_populates="comments")
    commenter = relationship("User", back_populates="comments")
