import time

def main():
    high_num = 0
    highest = 0
    for i in range(1,1000):
        count = 0
        x = i
        while x!=1:
            if x % 2==0:
                x = int(x / 2)
            else:
                x = x * 3 + 1
            count += 1
        if highest<count:
            high_num = i
            highest = count
    print(f"The highest number of steps was {highest} and of {high_num}.")
    
    
if __name__ == "__main__":
    main()