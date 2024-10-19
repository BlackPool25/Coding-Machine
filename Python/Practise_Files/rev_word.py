def new_sentence(string):
    words = string.split()
    new_str = ""
    for word in words:
        new_str += rev_word(word) + " "
    return new_str


def rev_word(word):
    return word[::-1]


def main():
    result = new_sentence(input("Enter string whose words need to be reversed: "))
    print(f"The result is {result}")


if __name__ == "__main__":
    main()