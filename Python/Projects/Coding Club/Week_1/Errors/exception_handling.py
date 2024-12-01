# exception = An event that interrupts the flow of a program
#                     (ZeroDivisionError, TypeError, ValueError)
#                     1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")

finally: # Always executes no matter if the block raises error or not
    print("Do some cleanup here")