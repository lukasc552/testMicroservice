from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import model, schema, services
from database import MySession, engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = MySession()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {}


@app.get('/posts')
def get_all_posts(db: Session = Depends(get_db), limit: int = 10):
    return services.get_posts(db=db, limit=limit)


@app.post('/posts')
def create_post(post: schema.BasePost, db: Session = Depends(get_db)):
    return services.create_post(db=db, post=post)


@app.get('/posts/{postId}')
def get_post(postId: int, db: Session = Depends(get_db)):
    return services.get_post_by_id(db=db, postId=postId)


@app.get('/users/{userId}/posts')
def get_user_posts(userId: int, db: Session = Depends(get_db)):
    return services.get_post_by_userId(db=db, userId=userId)


@app.put('/posts/{postId}')
def put_post(postId: int, post: schema.BasePost, db: Session = Depends(get_db)):
    return services.update_post(db=db, post=post, postId=postId)


@app.delete('/posts/{postId}')
def delete_post(postId: int, db: Session = Depends(get_db)):
    services.delete_post(db=db, postId=postId)
