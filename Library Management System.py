class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print("Borrowed:", title)
                return
        print("Book not available")

    def show_books(self):
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(book.title, "-", status)


# Example
lib = Library()
lib.add_book(Book("Python", "Guido"))
lib.add_book(Book("AI", "John"))

lib.borrow_book("Python")
lib.show_books()