import random

from brain_games.engine.game_engine import run_game

RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100

QUESTIONS_LIMIT = 3
OPERATION_PLUS = '+'
OPERATION_MINUS = '-'
OPERATION_MULTIPLY = '*'
OPERATIONS = [OPERATION_MINUS, OPERATION_PLUS, OPERATION_MULTIPLY]

GAME_RULES = 'What is the result of the expression?'


def generate_game_round():
    number1 = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    number2 = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    operation = random.choice(OPERATIONS)
    question = '{number1} {operation} {number2}'.format(
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
    run_game(GAME_RULES, generate_game_round)
