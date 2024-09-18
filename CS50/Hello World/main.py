name = input("What is your name: ").strip().title() #Take Input
# print("Hello", name) #Output
# print("Hello " + name)
# print("Hello ", end = "")
# print(name)

first, last = name.split(" ")

#Removes Whitespaces
# name = name.strip().title()

#Capitalize
# name = name.capitalize()

#Title 
# name = name.title()

print(f"Hello {first}")