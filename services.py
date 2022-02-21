from sqlalchemy.orm import Session
from fastapi import HTTPException
import model, schema, extern


def get_posts(db: Session, limit = 10):
    return db.query(model.Post).limit(limit).all()


def create_post(db: Session, post: schema.BasePost):
    if isinstance(post.userId, int):
        if extern.validate_user(post.userId):
            new_post = model.Post(userId=post.userId, title=post.title, body=post.body)
            db.add(new_post)
            db.commit()
            db.refresh(new_post)
            return new_post
        else:
            raise HTTPException(status_code=404, detail="User not found")
    else:
        raise HTTPException(status_code=400, detail="User ID is not valid integer")


def update_post(db: Session, post: schema.BasePost, postId: int):
    post_to_update = db.query(model.Post).filter(model.Post.id == postId).first()
    if post_to_update is None:
        error_str = f'Post with id={postId} does not exist'
        raise HTTPException(status_code=404, detail=error_str)
    else:
        post_to_update.title, post_to_update.body = post.title, post.body
        db.commit()
        db.refresh(post_to_update)
    return post_to_update


def get_post_by_id(db: Session, postId: int):
    post = db.query(model.Post).filter(model.Post.id == postId).first()
    if post is None:
        post_found = extern.find_post_by_id(postId)
        if post_found:
            cache_post = schema.BasePost(userId=post_found.get('userId'),
                                         title=post_found.get('title'),
                                         body=post_found.get('body'))
            create_post(db=db, post=cache_post)
            return post_found
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    return post


def get_post_by_userId(db: Session, userId: int):
    post = db.query(model.Post).filter(model.Post.userId == userId).all()
    if post is None:
        return {}
    return post


def delete_post(db: Session, postId: int):
    post_to_delete = db.query(model.Post).filter(model.Post.id == postId).first()
    if post_to_delete is not None:
        db.delete(post_to_delete)
        db.commit()
