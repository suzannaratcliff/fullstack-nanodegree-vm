import sys

from sqlalchemy import Column, ForeignKey, Iteger, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalechemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'



class MenuItem(Base):
    __tablename__ = 'menu_item'





engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadat.create_all(engine)

