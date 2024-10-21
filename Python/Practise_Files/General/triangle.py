def main():
    size = int(input("Enter the size: "))
    for i in range(1,size+1):
        print(" " * (size-i),end="")
        print("*"*(2 * i - 1))
    

if __name__ == "__main__":
    main()

