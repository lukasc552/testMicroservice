from sqlalchemy.orm import Session

import model, schema, extern

# TODO nezabudnut error handling


# def get_posts(db: Session, limit = 10):
#     return db.query(model.Post).limit(limit).all()


def create_post(db: Session, post: schema.BasePost):
    if extern.validate_user(post.userId):
        new_post = model.Post(userId=post.userId, title=post.title, body=post.body)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
    else:
        return {}


def update_post(db: Session, post: schema.BasePost, postId: int):
    post_to_update = db.query(model.Post).filter(model.Post.id == postId).first()
    # TODO osetrit vstupy
    post_to_update.title, post_to_update.body = post.title, post.body
    db.commit()
    db.refresh(post_to_update)
    return post_to_update


def get_post_by_id(db: Session, postId: int):
    # TODO osetrit ak taky neexistuje v DB vyhladat cez externu API
    post = db.query(model.Post).filter(model.Post.id == postId).first()
    if post is None:
        post_found = extern.find_post_by_id(postId)
        if post_found:

            # Cache
            # create_post(db=db, )

            return post_found
        else:
            return {}
    return post


def get_post_by_userId(db: Session, userId: int):
    post = db.query(model.Post).filter(model.Post.userId == userId).all()
    if post is None:
        return {}
    return post


def delete_post(db: Session, postId: int):
    post_to_delete = db.query(model.Post).filter(model.Post.id == postId).first()
    db.delete(post_to_delete)
    db.commit()
