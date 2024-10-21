def main():
    size = int(input("Enter the size: "))
    symbol = input("Enter the symbol to be printed.")
    column = 1
    for _ in range(0,size):
        for __ in range(0,column):
            print(symbol, end="")
        column += 1
        print()
    
if __name__ == "__main__":
    main()