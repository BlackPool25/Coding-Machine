import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    

def is_prime(num, prime_arr):
    for ele in prime_arr:
        if num%ele==0:
            return False
    return True


def main():
    clear()
    current_num = 2;
    size = int(input("Enter the size of the array: "))
    time1 = time.time()
    prime_arr = []
    while len(prime_arr) != size:
        if is_prime(current_num, prime_arr):
            prime_arr.append(current_num)
        current_num += 1
    print(prime_arr)
    time2 = time.time()
    print(f"The time taken is {time2-time1} seconds.")


if __name__ == "__main__":
    main()
        