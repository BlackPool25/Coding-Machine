import re
import sys

def main():
    email = input("Enter your email address: ")
    matches = re.search(r"(.*)@(.*)", email)
        
    print(f"Your username is {matches[1]} and the domain is {matches[2]}.")


if __name__ == "__main__":
    main()