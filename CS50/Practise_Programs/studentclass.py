class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house


    def __str__(self) -> str:
        return f"{self.name} from {self.house}."

    @classmethod
    def get(cls):
        name = input("Name: ").strip().title()
        house = input("House: ").strip().title()
        return cls(name, house)


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name


    @property
    def house(self):
        return self._house


    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
