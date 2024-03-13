import random as r

# Note:
#        in this program I intentionally used lots of functions just for practice and im well aware
#        for small projects it's a waste of energy as it complicates the program

print("Hello and welcome to my Rock Paper Scissors game!\n")

# here im defining what can you choose for the game
possibilities = ["rock", "paper", "scissors"]


# input ------------------------------

def choice_entry():
    while True:
        user_input = input("what's your choice? Rock, Paper or Scissors: ".lower())
        if user_input.isalpha():
            if user_input.strip() not in possibilities:
                print("Sorry but you're supposed to choose Rock, Paper or Scissors")
            else:
                return user_input
        else:
            print("Sorry, I didn't understand")

# process ------------------------------


def computers_selection():
    choices = ["rock", "paper", "scissors"]
    computer_choice = r.choice(choices)
    return computer_choice


def process(user_input, computer_choice):
    # rock > scissors , scissors > paper , paper > rock
    if user_input == computer_choice:
        return "It's a tie!"
    elif user_input == "rock" and computer_choice == "scissors" or \
            user_input == "scissors" and computer_choice == "paper" or \
            user_input == "paper" and computer_choice == "rock":
        return "You Win"
    else:
        return "You Lose"


# result ---------------------------

def results_and_replay():
    while True:
        print(process(choice_entry(), computers_selection()))
        replay = input("\nDo you want to play again? (Y/N)\n".lower())
        if replay == "y":
            results_and_replay()
        elif replay == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("\nPlease select either y or n\n")


results_and_replay()
