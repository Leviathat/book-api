from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import DatabaseError, NoResultFound


async def get_by_id(db: Session, book_id: int):
    """
    Either returns single models.Book class's object if it exists 
    or None if it's not 
    """
    return next(db).query(models.Book).get(book_id)


async def get_all(db: Session):
    """
    Return all rows in models.Book DB table
    """
    return next(db).query(models.Book).all()


async def create_book(db: Session, book: schemas.BookCreate):
    """
    Create new object after it's already validated by schema
    """
    db = next(db)
    db_book = models.Book(title=book.title, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


async def delete(db: Session, book: models.Book):
    """
    Deletes certain row based on it's id 
    """
    db = next(db)
    db.delete(book)
    db.commit()
    return book


async def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    """
    Sends INSERT query and return updated row
    """
    db = next(db)
    try:
        db.query(models.Book).filter(
            models.Book.id == book_id).update(values=dict(book))
        db.commit()
        return db.query(models.Book).filter(
            models.Book.id == book_id).first()
    except NoResultFound:
        return
