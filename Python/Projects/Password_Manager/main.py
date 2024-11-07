from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    key_file = open("key.key", "wb")
    key_file.write(key)
    key_file.close()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def view():
    with open("passwords.txt", 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split(": ")
            print(f"Username: {user}")
            print(f"Password: {str(fer.decrypt(passw.encode()))}\n")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as file:
        file.write(name + ": " + str(fer.encrypt(pwd.encode())) + "\n")


def check_key_file():
    open("key.key", "a").close()
    


master_pwd = input("What is the master password: ")
check_key_file()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

while True:
    mode = input("Would you like to add a new password(add) or view existing ones(view), press q to quit: ")
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Choice.")