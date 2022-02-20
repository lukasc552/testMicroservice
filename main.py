from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import model, schema, services, extern
from database import MySession, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# db = []
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
    if extern.validate_user(post.userId):
        return services.create_post(db=db, post=post)
    return {}



