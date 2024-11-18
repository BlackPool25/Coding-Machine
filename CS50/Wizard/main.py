import classes

def main():
    student = classes.Student('Harry', "Gryffindor")
    professor = classes.Professor("Severus", "Defense Aganist the Dark Arts")
    wizard = classes.Wizard('Albus')

    print(student)
    print(professor)
    print(wizard)

if __name__ == "__main__":
    main()