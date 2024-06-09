import sqlite3
from datetime import date, timedelta
from book import BookType, MAX_LOAN_TIME

class BorrowDAL:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def loan_book(self, custID, bookID, book_type):
        """
        Loan a book to a customer.
        """
        loan_date = date.today()
        max_loan_time = MAX_LOAN_TIME.get(book_type)
        if max_loan_time is None:
            raise ValueError("Invalid book type")
        return_date = loan_date + timedelta(days=max_loan_time)
        self.c.execute("INSERT INTO borrow (custID, bookID, loanDate, returnDate) VALUES (?, ?, ?, ?)",
                       (custID, bookID, loan_date, return_date))
        self.conn.commit()

    # Add other CRUD operations
