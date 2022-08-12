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
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(80), nullable=False)
    follower = relationship('Follower', backref='User', lazy=True)
    post = relationship('Post', backref='User', lazy=True)
    comment = relationship('Comment', backref='User', lazy=True)

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True) 

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer,primary_key=True)
    typeMedia = Column(Integer)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    media = relationship('Media', backref='Post', lazy=True)
    comment = relationship('Comment', backref='Post', lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column (Integer,primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey("user.id")) 
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')