class Student:
    def __init__(self, name, house) -> None:
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()
    # try:
    return Student(name,house)
    # except ValueError:
    

if __name__ == "__main__":
    main()