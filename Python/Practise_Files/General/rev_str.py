def main():
    usr_input = input("Enter the string: ").strip()
    print([char for char in usr_input if char.isalnum()])


if __name__ == "__main__":
    main()