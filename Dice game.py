import random
from colorama import Fore

blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
magenta = Fore.LIGHTMAGENTA_EX
reset = Fore.RESET


def dice():
    minimum = 1
    maximum = 6
    roll = random.randint(minimum, maximum)
    return roll


def rules():
    txt1 = f"1. The {magenta}cost{reset} of rolling a dice {red}increases{reset} with each round chosen to play."
    txt2 = f"2. By getting a {red}1{reset} your turn will be ended without any change in your score."
    txt3 = f"3. by getting a {yellow}6{reset} your cost of rolling will be reset."
    return txt1, txt2, txt3


# in here we ask the user(s) that how many players gonna be in the game and also providing a "rules" section to the
# user

def number_of_players():
    print("Hello and welcome to the dice game!\n")
    print(f"If you know the rules then lets get started if not then enter {green}rules{reset} to view them\n")
    while True:
        users = input("How many people wanna play? (2 - 4) ")
        if users.isdigit():
            users = int(users)
            if 2 <= users <= 4:
                return users
            else:
                print("This game only supports 2 to 4 players")
        elif users == "rules":
            txt1, txt2, txt3 = rules()
            print(f"\n{txt1}\n{txt2}\n{txt3}\n")
        else:
            print("Please enter a number")


# in here we get the players' score and format it into numbers (list => number)
# so we can show the scores in a fancy way

def score_formatting(score):
    formatted_scores = "\nScores: \n"
    for i, score in enumerate(score):
        formatted_scores += f"Player {i + 1}: {score}\n"
    return formatted_scores

# here we ask the user for the maximum score and then validating it


def maximum_score():
    while True:
        max_score = input("Set a goal: (the number that if you reach you'll win) ")
        if max_score.isdigit():
            max_score = int(max_score)
            if max_score > 0:
                return max_score
            elif max_score < 0:
                print("It's like that i say: yea yea, but if you wanna talk about it go and come back yesterday, hmm?")
            else:
                print("not 0 dude, you wanna win before you even get started? nah i wont let you")
        else:
            print("Please enter a number")


def players_turns(num_of_players):

    # creating a list comprehension and calling dice() function, also getting the maximum score (goal)

    player_scores = [0 for _ in range(num_of_players)]
    max_score = maximum_score()

    # here we have 3 loops
    # outer while loop check all the players' scores to be under the maximum score
    # the for loop is for switching between players
    # the inner while loop is for players' turn

    while max(player_scores) < max_score:
        for player_index in range(num_of_players):
            round_of_the_turns = 0

            while max(player_scores) < max_score:
                roll = dice()
                replay = input(f"\nDo you want to play player {magenta}{player_index + 1}{reset}? (Y/N) ").lower()
                if replay == "n":
                    break
                elif replay == "y":

                    if roll == 1:
                        print(f"{red}you got a 1! turn's over!{reset}")
                        break
                    elif roll == 6:
                        round_of_the_turns = 0
                        player_scores[player_index] += roll
                        print(f"\nyou got a {yellow}{roll}{reset}!")
                        print(score_formatting(player_scores))

                    else:

                        # here we subtract the cost and add the number the player got to their overall score
                        # we also add 1 to round_of_the_turns to count the times that player made move
                        # and in the end we display the overall score of all players

                        round_of_the_turns += 1
                        player_scores[player_index] -= round_of_the_turns
                        player_scores[player_index] += roll
                        print(f"\nyou got a {blue}{roll}{reset}!\n Number of moves (Cost) : {red}{round_of_the_turns}{reset}")
                        print(score_formatting(player_scores))

                else:
                    print("Sorry didnt understand your input")

    print(f"Your final score is {yellow}{score_formatting(player_scores)}{reset}")


players_turns(number_of_players())
