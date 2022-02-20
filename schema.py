from pydantic import BaseModel


class BasePost(BaseModel):
    userId: int
    title: str
    body: str


# class CreatePost(BasePost):
#     pass


class Post(BasePost):
    id: int