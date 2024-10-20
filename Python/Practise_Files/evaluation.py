import sys

def main():
    try:
        exp = input("Enter an expression: ")
        print(f"{exp} = {round(eval(exp), 3)}")
    except (NameError, SyntaxError):
        sys.exit("Invalid expression.")


if __name__ == "__main__":
    main()