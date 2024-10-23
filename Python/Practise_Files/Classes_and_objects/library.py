import sys

class Library:
    def __init__(self, location, size, filled = 0) -> None:
        self.location = location
        self.size = size
        self.filled = filled
        self.books = set()
    

    def add_book(self, book_name):
        if self.filled == self.size:
            raise BufferError("Library is full, cannot add more books.")
        self.books.add(book_name)
        self.filled += 1
    

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.discard(book_name)
            self.filled -= 1
        

    
    def display(self):
        print(f"Books in the library ({self.filled}/{self.size}): ")
        for book in self.books:
            print(f"- {book}")


def main():    
    
    shelf1 = Library("Ground Floor", 30)

    while True:

        options = [1, 2, 3, 4]
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Shelf")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except (ValueError, TypeError):
            print("Wrong choice, please enter a number.")
            continue

        if choice not in options:
            print("Wrong choice, try again.")
            continue

        match choice:
            case 1:
                shelf1.add_book(input("Enter the name of the book: "))
            
            case 2:
                shelf1.remove_book(input("Enter the name of the book: "))

            case 3:
                shelf1.display()

            case 4:
                print("This was the final library.")
                sys.exit(shelf1.display())
        if input("Continue (y or n): ").strip().lower() == "n":
            break
    

if __name__ == "__main__":
    main()
            

            
