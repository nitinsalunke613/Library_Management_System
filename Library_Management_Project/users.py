# Here we will use insert query to create new user for our Users table

from database import Database        # imported Database class from database module to use all the class objects


class UserService:
    def __init__(self):
        self.db = Database(host="localhost", user="root", password="NitinSQL@123", db="library")

    def create_user(self, email: str, password: str, is_admin: bool):
        query = "insert into Users (email, password, is_admin) values (%s, %s, %s)"  # MySQL query to insert a record
        params = (email, password, is_admin)
        self.db.execute_query(query, params)
        return {"message": "User created successfully"}

