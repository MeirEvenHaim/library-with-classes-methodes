from enum import Enum
import sqlite3

class BookType(Enum):
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

class Book:
    def __init__(self, name, author, type, year_of_publish):
        self.name = name
        self.author = author
        self.type = type
        self.year_of_publish = year_of_publish

class BookDAL:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def add_book(self, book):
        """
        Add a new book to the database.
        """
        self.c.execute("INSERT INTO book (name, author, type, year_of_publish) VALUES (?, ?, ?, ?)",
                       (book.name, book.author, book.type.value, book.year_of_publish))
        self.conn.commit()

    def get_all_books(self):
        """
        Retrieve all books from the database.
        """
        self.c.execute("SELECT * FROM book")
        return self.c.fetchall()

    # Add other CRUD operations
