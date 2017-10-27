from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('mysql+mysqldb://root@localhost:3306/blog')

Base = declarative_base()

class User(Base):

	__tablename__ = 'users'
