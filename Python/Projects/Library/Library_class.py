class Library:
    def __init__(self, location, size, filled = 0) -> None:
        self.location = location
        self.size = size
        self.filled = filled
        self.books = dict()
        self.current_book = 1
    

    def add_book(self, book_name):
        if self.filled == self.size:
            raise BufferError("Library is full, cannot add more books.")
        elif book_name in self.books:
            self.books[book_name].append(self.current_book)
            self.filled += 1
            self.current_book += 1
        else:
            self.books[book_name] = [self.current_book]
            self.filled += 1
            self.current_book += 1
    

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.pop(book_name)
            self.filled -= 1
        

    
    def display(self):
        print(f"Books in the library ({self.filled}/{self.size}): ")
        for book in self.books:
            print(f"- {book}")