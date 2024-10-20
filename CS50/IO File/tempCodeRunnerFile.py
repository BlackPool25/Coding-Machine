file_name = input("Enter file name: ")

with open(file_name, "a") as file:
    while True:
        name = input("What is your name: ")
        file.write(f"{name}\n")
        if input("Enter more names y or n: ").lower().strip() == "n":
            break