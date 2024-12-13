# Here we will create the Base Models of our tables(So we can give our data as a body in Swagger Ui)

from pydantic import BaseModel           # pydantic is useful for data validation


class CreateUserRequest(BaseModel):
    email: str
    password: str
    is_admin: bool = False


class AddBookRequest(BaseModel):
    title: str
    author: str


class BorrowRequest(BaseModel):
    user_id: int
    book_id: int
    start_date: str
    end_date: str


class UpdateBorrowRequest(BaseModel):
    status: str

