def check(usr_inp):
    stack = []
    for char in usr_inp:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack or not is_match(stack.pop(), char):
                return False
    return True
            

def is_match(opening,closing):

    key_value = {
                "(" : ")",
                "{" : "}",
                "[" : "]"
                 }
    
    return key_value[opening] == closing


def main():

    usr_inp = input("Enter the experession: ")
    
    if check(usr_inp):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()