from client import Client, ClientDAL
from book import Book, BookDAL, BookType
from borrow import BorrowDAL
import sqlite3
from datetime import date, timedelta

class LibraryApp:
    def __init__(self, db_name):
        self.db_name = db_name
        self.client_dal = ClientDAL(self.db_name)
        self.book_dal = BookDAL(self.db_name)
        self.borrow_dal = BorrowDAL(self.db_name)

    def add_customer(self, name, city, age):
        """
        Add a new customer to the library system.
        """
        new_client = Client(name, city, age)
        self.client_dal.add_client(new_client)
        print("Customer added successfully!")

    def add_new_book(self, name, author, book_type, year_of_publish):
        """
        Add a new book to the library system.
        """
        new_book = Book(name, author, book_type, year_of_publish)
        self.book_dal.add_book(new_book)
        print("Book added successfully!")

    # Add other functionalities as per your requirements

def main():
    db_name = 'library.db'
    app = LibraryApp(db_name)

    # Example usage
    app.add_customer("John Doe", "New York", 30)
    app.add_new_book("Python Basics", "John Smith", BookType.TYPE_1, 2020)

if __name__ == "__main__":
    main()
