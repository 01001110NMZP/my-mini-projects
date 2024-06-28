import random
import time

# values ----------------------------------

OPERATORS = ["*", "-", "+"]
MIN_OPERAND = 3
MAX_OPERAND = 12
NO_OF_QUESTIONS = 1

# operations ------------------------------


def problem_generator():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = f"{str(left)} {operator} {str(right)}"
    result = eval(expression)

    return expression, result


input("press Enter to start")
print("------------------------")
start_time = time.time()


def get_value():
    for i in range(NO_OF_QUESTIONS):
        expression, result = problem_generator()
        while True:
            try:
                answer = int(input(f"Problem #{i + 1}: {expression} = "))
                if answer == result:
                    break
                elif answer != result:
                    print("Incorrect")
                else:
                    print("Invalid input")
            except ValueError:
                pass
    end_time = time.time()
    total_time = end_time - start_time
    print("------------------------")
    print(f"Well done! you did it in {total_time:.2f} seconds!")


get_value()
