import sys

def dupe_finder(char_list):
    seen = set()
    for item in char_list:
        if item in seen:
            return item
        seen.add(item)
    return None


def clean(string):
    return ''.join(char for char in string if char.isalnum())


def main():
    try:
        list1 = list(clean(input("Enter a integer list: ").strip().split()))
    except (ValueError):
        sys.exit("Invalid input.")
    print(f"The first duplicate is {dupe_finder(list1)}")
    

if __name__ == "__main__":
    main()
    