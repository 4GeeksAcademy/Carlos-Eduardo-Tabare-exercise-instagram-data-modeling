import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """



class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(120))
    lastname= Column(String(120))
    email = Column(String(100), unique=True, nullable=False)
    comentarios = relationship('Comment', backref="users")
    posts = relationship('Post', backref="users")
    followers = relationship('Follower', backref="users")

class Comment(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    posts = relationship('Comment', backref="posts")
    media = relationship('Media', backref="posts")

class Media(Base):
    __tablename__='medias'
    id = Column(Integer, primary_key=True)
    type = Column(String(100))
    url = Column(String(100))
    post_id = Column(Integer, ForeignKey('posts.id'))

class Follower(Base):
    __tablename__='followers'
    user_from_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('users.id'), primary_key=True)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e 
