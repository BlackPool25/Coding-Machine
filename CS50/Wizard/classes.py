class Wizard:
    def __init__(self, name) -> None:
        if not name:
            raise ValueError("Missing name.")
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} is a wizard."


class Student(Wizard):
    def __init__(self, name, house) -> None:
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

    ...