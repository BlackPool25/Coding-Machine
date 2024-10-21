class Human:
    def __init__(self, heart):
        self.num_nose = 1
        self.num_eyes = 2
        self.num_heart = heart
    

    def eat(self):
        print("I can eat")


    def work(self):
        print("I can work")
    

class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name


    def work(self):
        super().work()
        print("I can code")

    
    def display(self):
        print(f"Hello I am {self.name} and I have {self.num_heart} heart.")


def main():
    male1 = Male("Shreyas", 1)
    male1.display()

if __name__ == "__main__":
    main()