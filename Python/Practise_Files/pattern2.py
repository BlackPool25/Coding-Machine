def print_pat(symbol,size):
    j = size
    i = 1
    for _ in range(0,size):
        print(" " * j, end="")
        print((symbol+" ") * i, end = "")
        i += 1
        j -= 1
        print()



def main():
    size = int(input("Enter the size: "))
    symbol = input("Enter the symbol: ")
    print_pat(symbol, size)


if __name__ == "__main__":
    main()