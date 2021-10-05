import random

from brain_games.scripts.games.common_game import common_game

QUESTIONS_LIMIT = 3
OPERATION_PLUS = '+'
OPERATION_MINUS = '-'
OPERATION_MULTIPLY = '*'
OPERATIONS = [OPERATION_MINUS, OPERATION_PLUS, OPERATION_MULTIPLY]


def generator():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = OPERATIONS[random.randint(0, 2)]
    question = 'Question: {number1} {operation} {number2}'.format(
        number1=number1, number2=number2, operation=operation)

    correct_answer = False
    if operation == OPERATION_PLUS:
        correct_answer = number1 + number2
    elif operation == OPERATION_MINUS:
        correct_answer = number1 - number2
    elif operation == OPERATION_MULTIPLY:
        correct_answer = number1 * number2

    return question, str(correct_answer)


def calc_game():
    common_game('What is the result of the expression?', generator)
