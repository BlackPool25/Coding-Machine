# Importing the math module
import math

# Introduction message
print("Welcome to the Python Math Program!")
print("Let's explore arithmetic operators, built-in functions, and the math module.\n")

# --- Arithmetic Operators ---
print("**Arithmetic Operators**")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Integer Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}\n")

# --- Built-in Math Functions ---
print("**Built-in Math Functions**")
x = -25
y = 16
print(f"Absolute value of {x}: {abs(x)}")
print(f"Power (2^3): {pow(2, 3)}")
print(f"Maximum of (3, 7, 2): {max(3, 7, 2)}")
print(f"Minimum of (3, 7, 2): {min(3, 7, 2)}\n")

# --- Using Math Module ---
print("**Math Module Functions**")
angle_deg = 45
y = 16
angle_rad = math.radians(angle_deg)  # Convert degrees to radians
print(f"Square root of {y}: {math.sqrt(y)}")
print(f"Sine of {angle_deg} degrees: {math.sin(angle_rad)}")
print(f"Cosine of {angle_deg} degrees: {math.cos(angle_rad)}")
print(f"Logarithm (base e) of 10: {math.log(10)}")
print(f"Value of Pi: {math.pi}")
print(f"Value of e: {math.e}\n")

# --- Circumference and Area of a Circle ---
print("**Circumference and Area of a Circle**")
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Circumference of the circle: {circumference:.2f}")
print(f"Area of the circle: {area:.2f}\n")

# --- Hypotenuse of a Right Triangle ---
print("**Hypotenuse Calculation**")
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
# Alternatively: math.hypot(side_a, side_b)
print(f"The hypotenuse of the triangle is: {hypotenuse:.2f}\n")

print("Thank you for exploring math in Python!")
