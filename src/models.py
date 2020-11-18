import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)



class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    postId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.userId'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    mediatId = Column(Integer, primary_key=True)
    postType = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    postId = Column(Integer, ForeignKey('post.postId'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    commentId = Column(Integer, primary_key=True)
    commentText = Column(String(250), nullable=False)
    userId = Column(Integer, ForeignKey('user.postId'))
    postId = Column(Integer, ForeignKey('post.postId'))
    post = relationship(Post)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')