# Here we will use insert and select query to create new user for our Users table

from database import Database         # imported Database class from database module to use all the class objects


class BookService:
    def __init__(self):
        self.db = Database(host="localhost", user="root", password="NitinSQL@123", db="library")

    def add_book(self, title: str, author: str):
        query = "insert into Books (title, author) values (%s, %s)"      # MySQL query to insert a record
        params = (title, author)
        self.db.execute_query(query, params)
        return {"message": "Book added successfully"}

    def list_books(self):
        query = "select * from Books"                    # MySQL query to retrieve all the data
        books = self.db.fetch_all(query)
        return {"List of Books": books}

