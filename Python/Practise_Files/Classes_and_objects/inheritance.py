class Human:
    def __init__(self):
        self.num_nose = 1
        self.num_eyes = 2
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
    

class Male(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def work(self):
        super().work()
        print("I can code")


def main():
    male1 = Male("Shreyas")
    print(male1.name)

if __name__ == "__main__":
    main()