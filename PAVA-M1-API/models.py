from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
    email = Column(String,index=True)

class Queries(Base):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String,index=True)
    date = Column(String,index=True)
    time = Column(String,index=True)


