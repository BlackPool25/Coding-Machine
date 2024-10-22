class Human:
    def __init__(self) -> None:
        self.num_eyes = 2
        self.num_nose = 1

    
    def work(self):
        print("I can work")

    
class Male:
    def __init__(self, name) -> None:
        self.name = name

    
    def flirt(self):
        print("I can flirt")
        
    
    def work(self):
        print("I can code")
    

class Boy(Human, Male):
    def sleep(self):
        print("I can sleep")

    
    def work(self):
        print("I can test")
    

def main():
    boy1 = Boy()
    boy1.work()
    print(boy1.num_eyes)


if __name__ == "__main__":
    main()