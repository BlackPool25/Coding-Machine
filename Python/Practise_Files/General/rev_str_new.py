def clean(string):
    return "".join(char for char in string if char.isalnum())


def main():
    usr_str = input("Enter a string: ").strip().lower()
    clean_str = clean(usr_str)
    print(f"The reverse of the string is {usr_str[::-1]}")
    if usr_str != clean_str:
        print(f"And the reverse without non aplhanumeric characters is {clean_str[::-1]}")
    if clean_str == clean_str[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
    

if __name__ == "__main__":
    main()