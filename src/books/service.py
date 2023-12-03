from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import DatabaseError, NoResultFound


async def get_by_id(db: Session, book_id: int):
    return next(db).query(models.Book).get(book_id)


async def get_all(db: Session):
    return next(db).query(models.Book).all()


async def create_book(db: Session, book: schemas.BookCreate):
    db = next(db)
    db_book = models.Book(title=book.title, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


async def delete(db: Session, book: models.Book):
    db = next(db)
    db.delete(book)
    db.commit()
    return book


async def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    db = next(db)
    try:
        db.query(models.Book).filter(
            models.Book.id == book_id).update(values=dict(book))
        db.commit()
        return db.query(models.Book).filter(
            models.Book.id == book_id).first()
    except NoResultFound:
        return
