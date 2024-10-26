import sys
from Library_class import Library


def manage_library(shelf):
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
                shelf.add_book(input("Enter the name of the book: ").strip().title())
            
            case 2:
                shelf.remove_book(input("Enter the name of the book: ").strip().title())

            case 3:
                shelf.display()

            case 4:
                print("This was the final library.")
                shelf.display()
                break


def main():    
    shelf1 = Library("Ground Floor", 30)
    manage_library(shelf1)

    
        
    

if __name__ == "__main__":
    main()
            

            
