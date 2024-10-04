import time
import math

def main():
    k = 1
    result = []
    i = 1
    while True:
        for _ in range(1, pow(2, k-1)+1):
            result.append(pow(2,k) - 1)
        k += 1
        print(result)
        time.sleep(1)
        del result[0]
        i += 1

if __name__ == "__main__":
    main()