import unittest
from math_quiz import (
    generate_random_integer,
    generate_random_operator,
    generate_problem_and_answer,
)

class TestMathQuiz(unittest.TestCase):
    def test_generate_random_integer(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        valid_operators = ['+', '-', '*']
        for _ in range(1000):
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators)

    def test_generate_problem_and_answer(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (7, 3, '+', '7 + 3', 10),
            (7, 3, '-', '7 - 3', 4),
            (7, 3, '*', '7 * 3', 21),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem_str, correct_answer = generate_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem_str, expected_problem)
            self.assertEqual(correct_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
