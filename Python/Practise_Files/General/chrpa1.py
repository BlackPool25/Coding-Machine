def main():
    size = int(input("Enter the size: "))
    num = 65
    column = 1
    for _ in range(0,size):
        for __ in range(0,column):
            print(chr(num), end="")
            num += 1
        column += 1
        print()


if __name__ == "__main__":
    main()