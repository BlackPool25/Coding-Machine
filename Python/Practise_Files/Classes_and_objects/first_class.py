class Instructor:
    def __init__(self,instructor_name, address):
        self.name = instructor_name
        self.address = address
        

def main():
    instructor_1 = Instructor("Shreyas", "Bangalore")
    print(instructor_1.name)


if __name__ == "__main__":
    main()