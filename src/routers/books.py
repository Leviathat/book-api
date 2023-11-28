from fastapi import APIRouter, Depends
from src.books.schemas import (
    BookBase,
    BookResponse,
    BookCreate
)
from src.books.dependencies import (
    valid_book,
    valid_book_id,
    get_all,
    delete_by_id
)

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.get("/", response_model=list[BookResponse])
async def get_all(books: BookBase = Depends(get_all)):
    return books


@router.get("/{book_id}", response_model=BookResponse)
async def get_book_by_id(book: BookBase = Depends(valid_book_id),):
    return book


@router.post("/", response_model=BookResponse)
async def create_book(book: BookCreate = Depends(valid_book),):
    return book


@router.delete("/{book_id}", response_model=BookResponse)
async def delete_book_by_id(book: BookBase = Depends(delete_by_id),):
    return book
