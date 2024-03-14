import os


# process
def view():
    data_size = os.path.getsize("data.txt")
    if data_size == 0:
        print("\nThere's nothing to show here, make your first username with its password")
    else:
        with open("data.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                username, password = data.split("|")
                print(f"Username: {username} | Password: {password}".strip())


def add():
    username = input("what's the username? ")
    password = input("what's the password? ")
    with open("data.txt", "a") as f:
        f.write(f"{username}|{password}\n")


def reset():
    user_choice = input("Which data you want to reset: passwords or master key? (p, m) ")
    if user_choice == "p":
        with open("data.txt", "w") as f:
            f.write("")
        print("\nall usernames and passwords have been deleted")
    elif user_choice == "m":
        with open("masterKey.txt", "w") as f:
            f.write("")
        print("\nmaster key has been reset")


# interface

def entry():
    while True:
        user_choice = input("\nHello, what do want to do? (add, view, reset, exit): ")
        if user_choice == "exit":
            quit()
        if user_choice == "add":
            add()
        elif user_choice == "view":
            view()
        elif user_choice == "reset":
            reset()
        else:
            print("sorry, I didn't understand")


def authentication():
    master_key = input("Set the master key: ")
    with open("masterKey.txt", "w") as f:
        f.write(master_key)

    while True:
        user_input = input("Enter the master key: ")
        with open("masterKey.txt", "r") as key:
            stored_master_key = key.read().strip()
            if stored_master_key == user_input:
                entry()
            else:
                print("Wrong master key")


authentication()
