class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    

    def area_rectangle(self):
        return self.length * self.breadth


def main():
    length1, breadth1 = map(float, input("Enter the length and breadth: ").strip().split())
    rectangle1 = Rectangle(length1, breadth1)
    print(f"Area = {rectangle1.area_rectangle()}")


if __name__ == "__main__":
    main()