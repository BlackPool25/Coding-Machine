import sys
from tabulate import tabulate
import csv

def main():
    check_cmdl_arg()
    table = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
        print(tabulate(table[1:], table[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_cmdl_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments!")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments!")
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a csv File")

if __name__ == "__main__":
    main()