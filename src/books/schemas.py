import pydantic
from datetime import date


class BookBase(pydantic.BaseModel):
    title: str = pydantic.Field(min_length=1, max_length=128)
    description: str = pydantic.Field(min_length=1, max_length=128)


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int = pydantic.Field()


class Book(BookBase):
    id: int
    # author_id: int

    class Config:
        orm_mode = True
