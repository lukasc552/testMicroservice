from pydantic import BaseModel


class BasePost(BaseModel):
    userId: int
    title: str
    body: str


class Post(BasePost):
    id: int