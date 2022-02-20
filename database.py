from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = "sqlite:///./sqlDB.db"

engine = create_engine(URL)
MySession = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()
