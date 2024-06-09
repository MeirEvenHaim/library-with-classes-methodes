import unittest
from client import Client, ClientDAL
from book import Book, BookDAL, BookType
from borrow import BorrowDAL, MAX_LOAN_TIME

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.db_name = ':memory:'
        self.client_dal = ClientDAL(self.db_name)
        self.book_dal = BookDAL(self.db_name)
        self.borrow_dal = BorrowDAL(self.db_name)

    def test_add_client(self):
        client = Client("John Doe", "New York", 30)
        self.client_dal.add_client(client)
        clients = self.client_dal.get_all_clients()
        self.assertEqual(len(clients), 1)

    def test_add_book(self):
        book = Book("Python Basics", "John Smith", BookType.TYPE_1, 2020)
        self.book_dal.add_book(book)
        books = self.book_dal.get_all_books()
        self.assertEqual(len(books), 1)

    def test_loan_book(self):
        client = Client("Jane Doe", "Los Angeles", 25)
        self.client_dal.add_client(client)
        book = Book("Python Advanced", "Jane Smith", BookType.TYPE_2, 2021)
        self.book_dal.add_book(book)
        self.borrow_dal.loan_book(client.id, book.id, book.type)
        loans = self.borrow_dal.get_all_loans()
        self.assertEqual(len(loans), 1)
        self.assertEqual(loans[0][0], client.id)
        self.assertEqual(loans[0][1], book.id)

    # Add more unit tests for other methods

if __name__ == '__main__':
    unittest.main()
