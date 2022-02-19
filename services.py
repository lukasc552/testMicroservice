from sqlalchemy.orm import Session

import model, schema


def get_posts(db: Session, limit = 10):
    return db.query(model.Post).limit(limit).al()

def create_post(db: Session, post: schema.CreatePost):
    new_post = model.Post(title=post.title, body=post.body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
