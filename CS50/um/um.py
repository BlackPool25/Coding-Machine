import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    number = 0
    search = re.findall(r"[ ,.](um)[ ,.]", s, re.IGNORECASE)
    for _ in search:
        number += 1
    return number


if __name__ == "__main__":
    main()
