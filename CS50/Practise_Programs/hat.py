import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


def main():
    Hat.sort("Harry")


if __name__ == "__main__":
    main()