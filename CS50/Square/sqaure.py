import time

t1 = time.time()
def main():
    user_input = int(input("What is the size of the square: "))
    print_square(user_input)
    t2 = time.time()
    print(f"Time Taken = {t2-t1}")


def print_square(n):
    for rows in range(n):
        for columns in range(n):
            print("#", end = "")
            # time.sleep(0.1)
        print()

main()