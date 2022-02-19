from pydantic import BaseModel


class BasePost(BaseModel):
    title: str
    body: str

class CreatePost(BasePost):
    pass

class Post(BasePost):
    id: int
    userId: int