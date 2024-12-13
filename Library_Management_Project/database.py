# Here we are creating a MySQL connection with Python and using Utility methods

import MySQLdb              # Imported MySQLdb to use the dependencies of MySQL


# PDBC and use of Utility Methods

class Database:
    def __init__(self, host: str, user: str, password: str, db: str):
        self.connection = MySQLdb.connect(host=host, user=user, passwd=password, db=db)
        self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)

    def execute_query(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params)             # to execute the query
            self.connection.commit()                       # commit to apply changes
        except Exception as e:
            self.connection.rollback()            # if any error found then it will Roll back the executed query
            raise e

    def fetch_all(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()         # To retrieve all the data
        except Exception as e:
            raise e

    def fetch_one(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()         # To retrieve single record
        except Exception as e:
            raise e

    def __del__(self):
        self.cursor.close()
        self.connection.close()           # closing of connection


# try : to find an error in the field
# except : to print or show that error message (Explicit try and except won't terminate our programme and will
# move to next)

