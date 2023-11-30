import pydantic


class BookBase(pydantic.BaseModel):
    """
    Model with basic attributes to be represented
    """
    title: str = pydantic.Field(min_length=1, max_length=128)
    description: str = pydantic.Field(min_length=1, max_length=128)


class BookCreate(BookBase):
    """
    Model to obtain input data during new book creation
    """
    pass


class BookUpdate(BookBase):
    """
    Model to obtain input data during updating already existing book  
    """
    pass


class BookResponse(BookBase):
    """
    Model to represent all response data
    """
    id: int


class Book(BookBase):
    """
    Model used for obtain returned data from DB 
    """
    id: int

    class Config:
        orm_mode = True
