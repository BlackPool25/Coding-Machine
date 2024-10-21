def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Replace a with b and b with a % b (remainder)
    return a


def main():
    a, b = map(int, input("Enter two numbers: ").strip().split())
    print(f"The GCD of the numbers is {gcd(a,b)}.")


if __name__ == "__main__":
    main()