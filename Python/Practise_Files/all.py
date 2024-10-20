def main():
    usr_inp = int(input("Enter a number: "))
    if all([usr_inp>0, usr_inp%2==0]):
        print("It is even and positive")
    else:
        print("It might be odd or it might be negative.")
    

if __name__ == "__main__":
    main()