class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, title):
        if title not in self.books:
            self.books[title] = 0
            print(f'Book "{title}" added to the library.')
        else:
            print(f'Book "{title}" already exists in the library.')
    def borrow_book(self, title):
        if title in self.books:
            self.books[title] += 1
            print(f'Book "{title}" borrowed successfully.')
        else:
            print(f'Book "{title}" is not in the library.')
    def total_books(self):
        return len(self.books)
    def least_borrowed(self):
        if not self.books:
            print('No books in the library.')
            return
        min_borrow = min(self.books.values())
        least_borrowed_books = [title for title, count in self.books.items() if count == min_borrow]
        print(f'Least borrowed book(s) with {min_borrow} borrow(s): {least_borrowed_books}')
    def most_borrowed(self):
        if not self.books:
            print('No books in the library.')
            return
        max_borrow = max(self.books.values())
        most_borrowed_books = [title for title, count in self.books.items() if count == max_borrow]
        print(f'Most borrowed book(s) with {max_borrow} borrow(s): {most_borrowed_books}')
    def never_borrowed(self):
        never_borrowed_books = [title for title, count in self.books.items() if count == 0]
        if never_borrowed_books:
            print('Books never borrowed:', never_borrowed_books)
        else:
            print('All books have been borrowed at least once.')
lib = Library()
lib.add_book('Harry Potter')
lib.add_book('The Hobbit')
lib.add_book('1984')
lib.add_book('The Great Gatsby')
lib.borrow_book('Harry Potter')
lib.borrow_book('Harry Potter')
lib.borrow_book('1984')
print('Total books:', lib.total_books())
lib.least_borrowed()
lib.most_borrowed()
lib.never_borrowed()
