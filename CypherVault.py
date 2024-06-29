import csv
import os
import sys
from colorama import Fore
from time import sleep
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# ------------------- colors
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
RESET = Fore.RESET
YELLOW = Fore.LIGHTYELLOW_EX
# ------------------- colors


class User:
    def __init__(self,
                 user_id: int, first_name: str,
                 last_name: str, *topics: str,
                 login_attempts: int = 0):

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.topics = topics

    def describe_user(self):
        text: str = (f"User ID: {self.user_id}"
                     f"\n First Name: {self.first_name}"
                     f"\n Last Name: {self.last_name}"
                     f"\n Interested Topics: {', '.join(self.topics).title()}\n")

        return text

    def greet_user(self):
        """returns a message greeting the user"""

        full_name = f"{self.first_name} {self.last_name}"
        text = f"Hello {full_name}! \nNice to meet you!"
        return text


# ---------------------------------------------------- end of the class

# ---------------------------------------------------- file checkers (start)


def file_checker() -> bool:
    """
    checks if the id.csv is there
    returns True anyway to make sure the file's there
    """
    if os.path.exists('id.txt'):
        return True
    else:
        with open('id.txt', 'w') as id_file:
            id_file.write('1')
            return True


def id_generator() -> int:
    """
    generates an id in this work flow:

    1. retrieves the id from the id.csv file and increments it by 1
    2. returns the new id
    4. overwrites the id.csv with the new id
    """

    # checks if "id.txt" is there, and create it if it isn't
    if file_checker():

        with open('id.txt', 'r') as id_reader:

            # assigning the content (last id) of "id.txt" as an int variable
            user_id = id_reader.read()
            int_id: int = int(user_id)

            with open('id.txt', 'w') as id_writer:
                id_writer.write(str(int_id + 1))  # incremented old id by 1 and changed it to str

            return int_id


def password_checker(user_id: int) -> bool:
    """checks the correction of the given password"""
    # source tutorial vid: https://www.youtube.com/shorts/n35w446_pgY

    load_dotenv()
    user_password = os.getenv("USER{}".format(user_id))

    # to ask for the correct password several times
    for _ in range(5):
        password: str = input(f"\nPlease enter the {YELLOW}exact{RESET} password"
                              f" for user with ID {MAGENTA}{user_id}{RESET}: ")

        if user_password != password:
            print(f"{RED}Wrong password{RESET}, Please try again")
        else:
            return True

    # 5 seconds delay in operation to let the user know they entered many wrong passwords
    # and then going back to the menu
    print(f"\n5 wrong passwords, Returning to menu.", end='')
    for _ in range(4):
        sleep(1)
        print('.', end='')
    print()
    main()


# ---------------------------------------------------- file checkers (end)

# ---------------------------------------------------- input (start)


def actions() -> int:
    """a sort of 'Menu' for program operations"""

    text: str = "\nWhat do you want to do?\n"\
                f"1. Make a {YELLOW}New Profile{RESET}\n"\
                f"2. Extract an existing profile\n"\
                f"3. {RED}Exit{RESET} the program\n"\
                f"4. {RED}Reset Data{RESET}\n"\
                f"Take action number: "

    try:
        action: int = int(input(text).strip())

        if action == 1:
            return 1  # New profile
        elif action == 2:
            return 2  # Load profile
        elif action == 3:
            # Exit
            print(f"\nAlright then, {MAGENTA}take care{RESET}!")
            sys.exit()
        elif action == 4:
            return 4  # Reset databases
        else:
            print("Sorry, I didn't understand")
    except ValueError:
        print("please only enter numbers and not letters")
    except Exception as e:
        print(f"somthing went wrong: {e.__class__.__name__}")


def get_info() -> tuple:
    """
    gets id for user from id_generator()
    asks user for the wanted info
    after validation, passes all the info in a tuple to info_saver()
    """

    user_id = id_generator()

    while True:
        try:
            # asks the user for data
            first_name: str = input("\nYour First Name: ").strip().title()
            last_name: str = input("Your Last Name: ").strip().title()
            interested_topic: str = input("Your favorite topic: ").strip().title()
            password: str = input(f"Set a password in {YELLOW}lowercase{RESET}"
                                  f" for your profile: ").strip().title()
            bio: str = input("Enter your bio: ").strip().title()

            # checks if the full name and interested topics are string (validating)
            if first_name.isalpha() and last_name.isalpha() and interested_topic.isalpha():
                return user_id, first_name, last_name, interested_topic, password, bio
            else:
                print(f"Please enter {RED}only letters{RESET}"
                      f" for your name and the topics you're interested in")

        except ValueError:
            print("Please enter alphabetical characters only")
        except Exception as e:
            print(f"Something went wrong : {e.__class__.__name__}")


# ---------------------------------------------------- input (end)

# ---------------------------------------------------- info manipulators - process (start)


def reset():
    text: str = (f"\nAre you sure you want to {RED}Reset{RESET}"
                 f" all and every data? \n"
                 f"{RED}This Can not be Undone{RESET}\n"
                 f"a) {GREEN}Yes{RESET}\tb) {RED}No{RESET}\n")

    confirmation: str = input(text).strip().lower()
    if 'a' in confirmation:
        # resetting user IDs
        with open('id.txt', 'w') as file:
            file.write('1')

        # resetting user profiles
        os.remove('users.csv')

        # resetting passwords
        os.remove('.env')

        print('\nReset Complete\n')

    elif 'b' in confirmation:
        print('\nReturning to the Menu')
        main()


def password_saver(password: str) -> str:
    """saves the given password to the .env file"""
    # source tutorial vid: https://www.youtube.com/shorts/n35w446_pgY

    # opens up the id.txt to find whose password is this
    with open("id.txt", "r") as user_id:
        user_id = user_id.read()

        last_user_id: int = int(user_id) - 1

        proper_env_user_name = "USER{}".format(last_user_id)

        # makes a safe, separate file for storing passwords
        with open('.env', 'a', ) as file:
            file.write(f"{proper_env_user_name}={password.lower()}\n")

    return f"{GREEN}Password saved successfully{RESET}"


def info_saver(user_id: int, first_name: str,
               last_name: str, topic: str,
               bio: str) -> str:
    """saves each user's profile in users.csv file"""

    with open('users.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        csv_writer.writerow([user_id, first_name, last_name, topic, bio])

    return ("Thank you!\n"
            f"{GREEN}Your information has been saved!{RESET}\n")


def load_request() -> int:
    """asks if the user want to load a certain profile by giving its id"""

    while True:
        try:
            requested_id: str = input('Give me the profile ID of'
                                      ' that user or "e" to Exit: ').strip()

            if requested_id == 'e':
                main()
            elif requested_id.isdigit():
                requested_id: int = int(requested_id)

                # check if the requested id is generated and available
                with open("id.txt", "r") as id_count:
                    last_id: int = int(id_count.read())

                    if requested_id == last_id and last_id == 1:
                        print(f"\nThere are {RED}no profiles{RESET} yet :/\n")

                    elif requested_id <= last_id - 1:
                        return requested_id

                    else:
                        print(f'\nSorry, The provided ID "{requested_id}"'
                              f' {RED}does not exist{RESET},'
                              f' try another id or enter "e" to exit\n')
            else:
                print('\nNumbers for IDs and "e" for Exit, right?\n')

        except ValueError:
            print("Please enter proper inputs")
        except Exception as e:
            print(f"Something went wrong: {e.__class__.__name__}")


def info_loader(requested_id) -> list:
    """retrieves each user's profile from users.csv"""

    with open("users.csv", "r") as profiles_csv:
        profile_reader = csv.reader(profiles_csv, delimiter=',')

        # checks each profile's id in O(n)
        for line in profile_reader:
            id_count = int(line[0])  # making IDs str -> int so the if statement can work

            if id_count == requested_id:
                return [line[0], line[1], line[2], line[3], line[4]]


# ---------------------------------------------------- info manipulators - process (end)

# ---------------------------------------------------- output (start)


def profile_display(user_id) -> str:
    """displays the given profile neatly"""
    profile = info_loader(user_id)

    # unpacking profile
    user_id: int = profile[0]
    first_name: str = profile[1]
    last_name: str = profile[2]
    topic: str = profile[3]
    bio: str = profile[4]

    seperator: str = "-" * 30

    text = f"\nUser: {first_name} {last_name}\n\n"\
           f"\tUser ID: {user_id}\n"\
           f"\tFavorite Topic: {topic}\n"\
           f"\t\nAbout:\n\t\t {bio}\n"

    return f"{seperator}\n{text}\n{seperator}"


def main() -> None:
    while True:
        action: int = actions()

        if action == 1:
            # gets the data provided by the user + generated ID
            user_id, first_name, last_name, interested_topic, password, bio = get_info()

            # passing first 4 items from info_loader() for saving
            print(f"\n{info_saver(user_id, first_name, last_name, interested_topic, bio)}")

            # passing the 'password' string to be stored separately
            print(f"{password_saver(password)}\n")

        elif action == 2:
            requested_id = load_request()

            # using if to make the program check the password
            if password_checker(requested_id):
                print(f"{GREEN}--- ACCESS GRANTED ---{RESET}")
                info_loader(requested_id)
                print(profile_display(requested_id))
        elif action == 4:
            reset()


# ---------------------------------------------------- output (end)


if __name__ == '__main__':
    main()
