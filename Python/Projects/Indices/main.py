import os 
import sys

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def main():
    clear()
    num = []
    result = []
    try:
        num.extend(map(int, input("Enter the nums: ").strip().split(",")))
        target = int(input("Enter the target number: "))
        for i in num:
            for j in num:
                if i+j == target:
                    if [num.index(i), num.index(j)] or [num.index(j), num.index(i)] not in result:
                        result.append([num.index(i), num.index(j)])

            
        print(f"The result list is {result[0]}")
    except (ValueError, KeyboardInterrupt):
        sys.exit()


if __name__ == "__main__":
    main()