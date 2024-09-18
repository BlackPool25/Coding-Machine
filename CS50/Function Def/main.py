def hello(to = "World"):
    print(f"Hello {to}!")
def main():
    name = input("What is your name? ")
    hello(name)
main()