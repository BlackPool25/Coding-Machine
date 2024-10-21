class Instructor:
    def __init__(self, name, address, followers = 0):
        self.name = name
        self.address = address
        self.followers = followers


    #expects subject_name as a string
    def display(self, subject):
        print(f"Hello, I am {self.name} and I teach {subject}")
    

    def update_follower(self):
        self.followers += 1

    
def main():
    instructor_1 = Instructor("Jenny", "Gurgaon", 15)
    print(instructor_1.name)
    instructor_1.display("Python")
    # instructor_2 = Instructor("Jiya", "Delhi")
    instructor_1.update_follower()
    print(instructor_1.followers)


if __name__ == "__main__":
    main()
        