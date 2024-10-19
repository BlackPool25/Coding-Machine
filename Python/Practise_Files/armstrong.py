def arms_checker(usr_input, length):
    result = 0
    for digit in usr_input:
        temp = 1
        digit = int(digit)
        for _ in range(0,length):
            temp*=digit
        result += temp
    return str(result)


def main():
    usr_input = str(int(input("Enter a number: ")))
    length = len(usr_input)
    check_value = arms_checker(usr_input, length)
    if check_value == usr_input:
        print("It is an armstrong number.")
    else:
        print("It is not an armstrong number.")

    
if __name__ == "__main__":
    main()