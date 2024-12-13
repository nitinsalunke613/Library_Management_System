# This is the main file where we will run our application using API endpoints

from fastapi import FastAPI
from tables import *
from users import UserService
from books import BookService
from borrow_books import BorrowService

# Creating an Instance of FastAPI class
app = FastAPI()

# Initialization of services
user_service = UserService()
book_service = BookService()
borrow_service = BorrowService()


@app.get("/")                        # (GET)To read the data
def root():
    return {"message": "Welcome to the Library Management System!"}


# User APIs to insert a User
@app.post("/users/create")           # (POST)To create new request
def create_library_user(user_request: CreateUserRequest):
    return user_service.create_user(user_request.email, user_request.password, user_request.is_admin)


# Book APIs to insert and retrieve Books
@app.post("/books/add")              # (POST)To create new request
def add_library_book(book_request: AddBookRequest):
    return book_service.add_book(book_request.title, book_request.author)


@app.get("/books")                   # (GET)To read the data
def get_all_books():
    return book_service.list_books()


# Borrow Request APIs to Create new borrow request, View borrow requests and Update the borrow requests
@app.post("/borrow_books/create")         # (POST)To create new request
def request_borrow(borrow_request: BorrowRequest):
    return borrow_service.borrow_book(borrow_request.user_id, borrow_request.book_id, borrow_request.start_date,
                                      borrow_request.end_date)


@app.get("/borrow_books")         # (GET)To read the data
def get_borrow_requests():
    return borrow_service.view_borrow_requests()


@app.put("/borrow_books/{request_id}")         # (POST)To create new request (Dynamic parameter)
def update_borrow_request(request_id: int, update_request: UpdateBorrowRequest):
    return borrow_service.process_borrow_request(request_id, update_request.status)

