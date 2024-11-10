import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value, inclusive.

    Parameter:
    min_value: The minimum value.
    max_value: The maximum value.

    Return:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random operator from '+', '-', '*'.

    Return:
    str: A random operator.
    """
    return random.choice(['+', '-', '*'])

def generate_problem_and_answer(num1, num2, operator):
    """
    Generate a math problem string and its correct answer based on the operator.

    Parameter:
    num1: The first number.
    num2: The second number.
    operator (str): The operator ('+', '-', '*').

    Return:
    tuple: A tuple containing the problem string and the correct answer.
    """
    problem_str = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    else:
        raise ValueError(f"Invalid operator: {operator}")
    return problem_str, correct_answer

def math_quiz():
    """
    Main function
    """
    score = 0
    total_questions = 5  # Set the number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and a random operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)
        operator = generate_random_operator()

        # Generate the problem and the correct answer
        problem_str, correct_answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem_str}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
