from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added.")

class Transaction:
    def __init__(self, transaction_id, user, book, issue_date):
        self.transaction_id = transaction_id
        self.user = user
        self.book = book
        self.issue_date = issue_date
        self.return_date = issue_date + timedelta(days=14)
        self.fine = 0

    def calculate_fine(self, return_date):
        delay = (return_date - self.return_date).days
        if delay > 0:
            self.fine = delay * 5  # $5 per day fine
        return self.fine

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def issue_book(self, user, book):
        if book.available:
            transaction = Transaction(len(self.transactions) + 1, user, book, datetime.now())
            book.available = False
            self.transactions.append(transaction)
            print(f"Book '{book.title}' issued to {user.name}.")
        else:
            print(f"Book '{book.title}' is not available.")

    def return_book(self, book, return_date):
        for transaction in self.transactions:
            if transaction.book == book:
                fine = transaction.calculate_fine(return_date)
                book.available = True
                print(f"Book '{book.title}' returned. Fine: ${fine}")

# Example Usage
library = Library()
book1 = Book(1, "1984", "George Orwell")
user1 = User(101, "Alice")

library.books.append(book1)
library.users.append(user1)

library.issue_book(user1, book1)
library.return_book(book1, datetime.now() + timedelta(days=16))  # 2 days late
