import random

from brain_games.scripts.games.common_game import common_game

RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def generator():
    number = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    question = '{number}'.format(number=number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


def even_game():
    common_game('Answer "yes" if the number is even, otherwise answer "no".',
                generator)
