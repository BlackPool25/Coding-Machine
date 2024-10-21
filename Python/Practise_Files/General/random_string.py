import string
import random

def random_str_gen(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))


def main():
    size = int(input("Enter the size: "))
    print(f"The random string is: {random_str_gen(size)}")


if __name__ == "__main__":
    main()