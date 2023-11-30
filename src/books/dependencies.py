from typing import Mapping, Annotated
from fastapi import HTTPException
from src.database import get_session
from . import models, schemas, service
from fastapi import Depends


async def get_all():
    session = get_session()
    return await service.get_all(session)


async def valid_book_id(book_id: int):
    session = get_session()
    book = await service.get_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="No book found")
    return book


async def delete_by_id(book_id: int):
    session = get_session()
    return await service.delete(session, book_id)


async def valid_book(book: schemas.BookCreate) -> models.Book:
    session = get_session()
    return await service.create_book(session, book)


async def valid_update_book(book_id: int, book: schemas.BookUpdate):
    session = get_session()
    return await service.update_book(session, book_id, book)
