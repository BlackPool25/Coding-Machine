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
        num.extend(map(int, input("Enter the nums: ").strip().split()))
        target = int(input("Enter the target number: "))
        for i in num:
            for j in num:
                if [num.index(i),num.index(j)] in num or [num.index(j),num.index(i)] in result:
                    continue
                elif i+j == target:
                    result.append([num.index(i), num.index(j)])
        print(f"The result list is {[ele for ele in result]}")
    except (ValueError, KeyboardInterrupt):
        sys.exit()


if __name__ == "__main__":
    main()