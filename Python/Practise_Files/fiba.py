import sys


def main():
    nterms = int(input("Enter the number of terms: "))
    n1, n2 = 0,1
    if nterms<1:
        sys.exit("Enter a valid number of terms.")
    elif nterms == 1:
        sys.exit(f"The fibanocci sequence of {nterms} terms is: \n[{n1}]")
    count = 0
    fiba = []
    print(f"The fibanocci sequence of {nterms} terms is: ")
    while count<nterms:
        fiba.append(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1
    print(fiba)

if __name__ == "__main__":
    main()