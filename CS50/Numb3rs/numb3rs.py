import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    pattern = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    matches = re.search(f"^{pattern}\.{pattern}\.{pattern}\.{pattern}$", ip)
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

