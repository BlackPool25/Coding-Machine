import sys
from Library_class import Library


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
                shelf1.add_book(input("Enter the name of the book: ").strip().title())
            
            case 2:
                shelf1.remove_book(input("Enter the name of the book: ").strip().title())

            case 3:
                shelf1.display()

            case 4:
                print("This was the final library.")
                shelf1.display()
                break
        
    

if __name__ == "__main__":
    main()
            

            
