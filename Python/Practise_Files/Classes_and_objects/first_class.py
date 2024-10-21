class Instructor:
    def __init__(self,instructor_name, address, followers = 0):
        self.name = instructor_name
        self.address = address
        self.followers = followers
        

def main():
    instructor_1 = Instructor("Shreyas", "Bangalore", 375)
    print(instructor_1.name , instructor_1.followers)
    
    instructor_2 = Instructor("Payal", "Delhi")
    print(instructor_2.name , instructor_2.followers)


if __name__ == "__main__":
    main()