class Circle:
    PI = 3.14159
    def __init__(self, radius):
        self.radius = radius


    def circumference(self):
        return 2 * self.PI * self.radius
    

    def area(self):
        return self.PI * (self.radius ** 2)



def main():
    circle1 = Circle(float(input("Enter the radius: ")))
    print("Area:", circle1.area())
    print("Circumference:", circle1.circumference())

if __name__ == "__main__":
    main()