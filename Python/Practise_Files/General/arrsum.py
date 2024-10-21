def add(a,b):
    return a+b


def main():
    list1 = list(map(int , input("Enter the first list: ").strip().split()))
    list2 = list(map(int , input("Enter the second list: ").strip().split()))
    added_list = sum(list(map(add, list1, list2)))
    print(added_list)


if __name__ == "__main__":
    main()