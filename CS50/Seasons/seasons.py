from datetime import date
import inflect
import sys

class Song:
    p = inflect.engine()

    def __init__(self, birthdate) -> None:
        self.birthdate = birthdate
        self.today = date.today()
    
    def date_in_song(self):
        delta = self.today-self.birthdate
        minutes = delta.days * 24 * 60

        return f"{self.p.number_to_words(minutes, andword="")} minutes"
    
    @property
    def birthdate(self):
        return self._birthdate
    
    @birthdate.setter
    def birthdate(self, birthdate):
        try:
            date1 = date.fromisoformat(birthdate)
        except ValueError:
            sys.exit("Invalid Input")
        self._birthdate = date1
    
    @classmethod
    def get(cls):
        return cls(input("Enter Birthdate: ").strip())


def main():
    min = Song.get()
    words = min.date_in_song()
    print(words)


if __name__ == "__main__":
    main()