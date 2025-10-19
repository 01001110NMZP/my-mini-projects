class Problem:
    _instances: list["Problem"] = []

    def __init__(self, question: str, correct_answer: str, answers: list[str]):
        self.question = question
        self.correct_answer = correct_answer  # stored as "1", "2", etc.
        self.answers = answers
        Problem._instances.append(self)

    def __del__(self):
        """Removes the instance when deleted."""
        if self in Problem._instances:
            Problem._instances.remove(self)

    @classmethod
    def all(cls) -> list["Problem"]:
        """Return all current Problem instances."""
        return cls._instances

    @classmethod
    def count(cls) -> int:
        """Return how many Problem instances exist."""
        return len(cls._instances)


def ask_questions() -> list[str]:
    """Iterate through all problems, ask user input, return their answers."""
    answers: list[str] = []

    for problem in Problem.all():
        print(f"\n{problem.question}\n")
        for ans in problem.answers:
            print(f"\t{ans}")

        while True:
            user_answer: str = input("\nEnter The Answer (1-4): ").strip()
            if user_answer in {"1", "2", "3", "4"}:
                answers.append(user_answer)
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")

        print("--------------------------------------")

    return answers


def result_stats(answers: list[str]) -> None:
    """Score is the sum of all chosen numbers, normalized."""
    max_score: int = Problem.count() * 4
    user_score: int = sum(int(a) for a in answers)
    percent: float = user_score * 100 / max_score

    print("\n-- Results (Stats) --\n")
    print(f"Highest possible score: {max_score}")
    print(f"Your score: {user_score}")
    print(f"Percentage: {percent:.2f}% | {user_score}/{max_score}")


def result_correctness(answers: list[str]) -> None:
    """Checks correctness against predefined correct answers."""
    correct = sum(1 for problem, ans in zip(Problem.all(), answers)
                  if ans == problem.correct_answer)

    max_score = Problem.count()
    percent = correct * 100 / max_score

    print("\n-- Results (Correctness) --\n")
    print(f"Highest possible score: {max_score}")
    print(f"Your correct answers: {correct}")
    print(f"Percentage: {percent:.2f}% | {correct}/{max_score}")


def main() -> None:
    # Problem instances (no need for external list)
    Problem("What year python was made?",
            "1",
            ["1. 1991",
             "2. 2001",
             "3. 1989",
             "4. 2006"])

    Problem("Who made python?",
            "1",
            ["1. Guido van Rossum",
             "2. James Gosling",
             "3. Dennis Ritchie",
             "4. Bjarne Stroustrup"])

    Problem("Which languages are famous to be used alongside python for enterprise AI/ML?",
            "2",
            ["1. R/Julia", "2. Java/C++", "3. R/C++", "4. Julia/Java"])

    Problem("Why python is used for AI instead of faster languages?",
            "3",
            ["1. It's easier",
             "2. Readability and debugging",
             "3. Faster for prototyping",
             "4. For scientists who don't have extended experience with low-level languages"])

    # Ask questions
    answers = ask_questions()

    # Choose result display
    print("\nWhich result do you want to see?\n1. Stats\n2. Correctness\n3. Both")
    while True:
        try:
            choice = int(input("Choose mode (1, 2, 3): "))
            if choice == 1:
                result_stats(answers)
                break
            elif choice == 2:
                result_correctness(answers)
                break
            elif choice == 3:
                result_stats(answers)
                print("--------------------------------------")
                result_correctness(answers)
                break
        except ValueError:
            pass
        print("Only enter 1, 2, or 3, please.")


if __name__ == "__main__":
    main()
