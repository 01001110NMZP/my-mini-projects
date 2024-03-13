from colorama import Fore

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
magenta = Fore.LIGHTMAGENTA_EX
reset = Fore.RESET


def new_game():
    answers = []
    question_number = 0
    for key in questions:
        print(key)
        transformer = ""
        corrected_answers = None
        for i in possible_answers[question_number]:
            transformer += i + "   "
            corrected_answers = transformer
        print(f"{corrected_answers}\n")
        answer = input(f"\n{white}your answer: {reset}")
        answers.append(answer.capitalize())
        question_number += 1
    return answers

# ---------------------


def process():
    correctness_percentage = 0
    correctness = [False, False, False, False]
    gathered_info = new_game()

    if gathered_info[0] == questions["Who created python? "]:
        correctness_percentage += 25
        correctness[0] = True
    if gathered_info[1] == questions["When python was created? "]:
        correctness_percentage += 25
        correctness[1] = True
    if gathered_info[2] == questions["Whats the python files' suffix? "]:
        correctness_percentage += 25
        correctness[2] = True
    if gathered_info[3] == questions["Is earth flat? "]:
        correctness_percentage += 25
        correctness[3] = True

    return correctness_percentage, correctness

# ---------------------


def results():

    correctness_percentage, correctness = process()
    num = 0
    print(f"----------------------\nYour answers are:")
    colored_correctness = ""
    for key, value in questions.items():
        if correctness[num]:
            colored_correctness = f"{green}{correctness[num]}{reset}"
        elif correctness[num] is False:
            colored_correctness = f"{red}{correctness[num]}{reset}"
        print(f"{white}{key} {magenta}{value}{reset} {colored_correctness}{reset}")
        num += 1

    if correctness_percentage == 100:
        print(f"you're {green}%100{reset} correct! hell yea!")
    elif correctness_percentage == 75:
        print(f"you're {blue}%75{reset} correct! almost there!")
    elif correctness_percentage == 50:
        print(f"you're {yellow}%50{reset} correct! half way there!")
    elif correctness_percentage == 25:
        print(f"you're {red}%25{reset} correct!, you just need some time, im sure of it!")
    else:
        print(f"you're {red}%0{reset} correct, you need more practice")

# ---------------------


def replay():
    results()
    while True:
        user_input = input("\nWould you like to play again? (Y or N) ")
        if user_input.capitalize() == "Y":
            results()
        elif user_input.capitalize() == "N":
            print("\nhope you enjoyed the test, cya!")
            break


questions = {
    "Who created python? ": "A",
    "When python was created? ": "B",
    "Whats the python files' suffix? ": "D",
    "Is earth flat? ": "B"
}

possible_answers = [
    ["A) Guido van Rossum", "B) Elon Musk", "C) Bill Gates", "D) Mark Zuckerburg"],
    ["A) 1989", "B) 1991", "C) 2000", "D) 2016"],
    ["A) python", "B) ptn", "C) thon", "D) py"],
    ["A) true", "B) false", "C) sometimes", "D) what's earth btw?"]
]

replay()
