class Instructor:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    
def main():
    instructor_1 = Instructor("Jenny", "Gurgaon")
    print(instructor_1.name)


if __name__ == "__main__":
    main()
        