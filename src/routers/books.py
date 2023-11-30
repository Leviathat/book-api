from fastapi import APIRouter, Depends
from src.books.schemas import (
    BookResponse,
    BookCreate
)
from src.books.dependencies import (
    valid_book,
    valid_book_id,
    get_all,
    delete_by_id,
    valid_update_book
)

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.get("/", response_model=list[BookResponse], status_code=200)
async def get_all(books: BookResponse = Depends(get_all),):
    """
    **Lists all Book model objects**
    """
    return books


@router.get("/{book_id}", response_model=BookResponse, status_code=200)
async def get_book_by_id(book: BookResponse = Depends(valid_book_id),):
    """
    **Refers single Book model object by id**
    """
    return book


@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate = Depends(valid_book)):
    """
    **Creates single Book model object based on input**
    """
    return book


@router.delete("/{book_id}", response_model=BookResponse, status_code=200)
async def delete_book_by_id(book: BookResponse = Depends(delete_by_id),):
    """
    **Deletes single Book model object by id**
    """
    return book


@router.put("/{book_id}", response_model=BookResponse, status_code=201)
async def update_book_by_id(book: BookResponse = Depends(valid_update_book),):
    """
    **Deletes single Book model object by id**
    """
    return book
