import random
from colorama import Fore


def main(computer_input, user_input):

    result = f"\nYou chose: {Fore.YELLOW}{user_input}{Fore.RESET}\nComputer chose: {Fore.YELLOW}{computer_input}{Fore.RESET}"

    if computer_input == "paper" and user_input == "scissors" or \
            computer_input == "rock" and user_input == "paper" or \
            computer_input == "scissors" and user_input == "rock":
        print(result)
        print(f"{Fore.BLUE}You win!{Fore.RESET}")
    elif computer_input == user_input:
        print(result)
        print(f"{Fore.MAGENTA}It's a tie!{Fore.RESET}")
    else:
        print(result)
        print(f"{Fore.RED}You lose!{Fore.RESET}\n")


# here we define the move of the computer to prevent any code duplication
choices = ["rock", "paper", "scissors"]
computer_input = random.choice(choices)

while True:

    continuing = input("Do you want to play again? (Y or N) ".lower())
    if continuing == "y":
        user_input = input("rock, paper or scissors: ")
        main(computer_input, user_input)
    elif continuing == "n" or continuing == "N":
        print("Thanks for playing")
        break
    else:
        print("invalid input")

