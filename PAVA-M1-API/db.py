from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Url_DB = 'postgresql://postgres:1245@localhost:5432/pavaApi'

engine = create_engine(Url_DB)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()