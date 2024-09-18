def calc(x,y):
    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "*":
        return x*y
    elif operator == "/":
        return x/y
    else:
        print("Invalid Input.")
        exit()
x = float(input("Enter the first variable: "))
y = float(input("Enter the second variable: "))
operator = input("Enter the operation(+,-,*,/): ")
z = calc(x,y)
# z= round(z,2)
print(f"The result is {z:.2f}")


