import random


def guessing_game():
    while True:
        try:
            # we need a min-max interval to mess with
            while True:
                entry_point = int(input("Set an entry point for the secret number: "))
                ending_point = int(input("Set an ending point for the secret number: "))

                # Logicalizing values

                if entry_point == ending_point:
                    print("Entry and ending points must not be the same")
                elif entry_point > ending_point:
                    print("Entry point should be smaller than the ending point")
                else:
                    break

            no_of_guesses = 0
            secret_number = random.randint(entry_point, ending_point)
            guess = 0
            while secret_number != guess:
                guess = int(input("What number do you think it is? "))
                no_of_guesses += 1
                if secret_number > guess:
                    print("Too low")
                elif secret_number < guess:
                    print("Too high")
                elif secret_number == guess:
                    return no_of_guesses

        except ValueError:
            print("Please enter an integer (or a number we could say)")


def computer_guess():
    while True:
        try:
            while True:
                min_range = int(input("Whats the minimum of your number's domain? "))
                max_range = int(input("Whats the maximum of your number's domain? "))

                # checking if the min and max values are logical
                if max_range == min_range:
                    print("Minimum and maximum numbers shouldn't be the same!")
                elif max_range < min_range:
                    print("Minimum numbers are usually smaller than maximum values right?")
                else:
                    break

            guess = random.randint(min_range, max_range)
            feedback = ''
            print(guess)
            while feedback != 'c':
                feedback = input("is it bigger, smaller or correct? (B, S, C)".lower())
                if feedback == 'b':
                    guess = guess - 1
                    print(guess)
                elif feedback == 's':
                    guess = guess + 1
                    print(guess)
            return guess

        except ValueError:
            print("Please enter a number")


print("Welcome to the guessing game(s) bundle\n\nwhich one do you wish to play?\n\
1. guessing game - user (you have to guess)\n2. guessing game - computer (computer guesses your number)\n")

while True:
    user_input = input("1 or 2? (enter 'exit' to well... exit) ")
    if user_input == "1":
        print(f"Congratulations!\nYou've done it in {guessing_game()} tries")
    elif user_input == "2":
        print(f"So {computer_guess()} was your numbah? cool")
    elif user_input == "exit":
        print("thanks for playing")
        break
    elif user_input == "exit":
        print("thanks for playing")
        break
