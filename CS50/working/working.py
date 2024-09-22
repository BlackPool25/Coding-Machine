import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    pattern = r"(1[0-2]|[0-9])(?:\:([0-5][0-9]))? (AM|PM)"
    if work_hours := re.search(f'{pattern} to {pattern}', s):

        hours1 = int(work_hours.group(1))
        if work_hours.group(2):
            mins1 = int(work_hours.group(2))
        else:
            mins1 = 0
        
        hours2 = int(work_hours.group(4))
        if work_hours.group(5):
            mins2 = int(work_hours.group(5))
        else:
            mins2 = 0

        if (work_hours.group(3) == "PM") and (1<=hours1<=11):
            hours1 += 12
        if (work_hours.group(6) == "PM") and (1<=hours2<=11):
            hours2 += 12

        return f"{hours1:02}:{mins1:02} to {hours2:02}:{mins2:02}"

    else:
        raise ValueError("Incorrect input")


if __name__ == "__main__":
    main()
