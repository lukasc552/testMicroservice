from sqlalchemy import Column, Integer, String
from database import Base


class Post(Base):
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    title = Column(String)
    body = Column(String)
