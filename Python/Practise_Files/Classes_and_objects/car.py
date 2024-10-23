class Car:
    def __init__(self, brand, max_speed, colour) -> None:
        self.brand = brand
        self.max_speed = max_speed
        self.colour = colour
    

    def describe(self):
        return f"The car is {self.colour} {self.brand} and it has a max speed of {self.max_speed} km/h."


def main():
    car1 = Car("Honda", 200, "Yellow")
    print(car1.describe())


if __name__ == "__main__":
    main()
