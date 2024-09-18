from tabulate import tabulate
import sys
import os

def take_input():
    try:
        key = int(input("What is the roll number of the student: "))
        value = []
        value.append(input("Enter the name of the student: ").title().strip())
        for i in range(1,4):
            usr_inpt = float(input(f"Enter the marks for subject {i}: "))
            assert (usr_inpt<=100) & (usr_inpt>=0)
            value.append(usr_inpt)
    except (TypeError, ValueError, AssertionError):
            sys.exit("Incorrect input.")
    return key,value
    

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def main():
    clear()
    try:
        student_dict = {}
        table = []
        headers = ["Roll number", "Name", "Subject 1", "Subject 2", "Subject 3"]
        while True:
            key, value = take_input()
            student_dict[key] = value
            table.append([key] + list(value))
            if input("Do you want to make another entry to the dictionary (y or no): ").lower().strip() == "y":
                continue
            break
        print(tabulate(table, headers, tablefmt="grid"))
    
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
