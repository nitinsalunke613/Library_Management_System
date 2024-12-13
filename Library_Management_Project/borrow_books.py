# Here we will use insert, select and update queries for borrow request of the Books

from database import Database


class BorrowService:
    def __init__(self):
        self.db = Database(host="localhost", user="root", password="NitinSQL@123", db="library")

    def borrow_book(self, user_id: int, book_id: int, start_date: str, end_date: str):

        # To check the borrow request for the book
        query_check = ("select * from borrow_requests WHERE book_id = %s AND "
                       "(%s BETWEEN start_date AND end_date OR %s BETWEEN start_date AND end_date)")
        check_params = (book_id, start_date, end_date)
        overlap = self.db.fetch_one(query_check, check_params)     # MySQL query to retrieve single record
        if overlap:
            return {"error": "Book is already borrowed for the given dates"}

        # Inserting the details to request to borrow a book
        query_insert = ("insert into borrow_requests (user_id, book_id, start_date, end_date, status) "
                        "values (%s, %s, %s, %s, 'Pending')")
        insert_params = (user_id, book_id, start_date, end_date)
        self.db.execute_query(query_insert, insert_params)
        return {"message": "Borrow request submitted successfully"}

    # To retrieve all the Book borrow requests
    def view_borrow_requests(self):
        query = "select * from borrow_requests"
        all_requests = self.db.fetch_all(query)          # MySQL query to retrieve all the data
        return {"all_borrow_requests": all_requests}

    # To process the borrow requests (either Approve or Deny)
    def process_borrow_request(self, request_id: int, status: str):
        query = "update borrow_requests SET status = %s WHERE id = %s"    # MySQL query to update a record
        params = (status, request_id)
        self.db.execute_query(query, params)
        return {"message": "Borrow request updated successfully"}

