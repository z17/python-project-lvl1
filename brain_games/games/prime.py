import math
import random

from brain_games.games.common_game import common_game

RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 500


def is_prime_number(number):
    middle = int(math.ceil(number / 2) + 1)
    for i in range(2, middle):
        if number % i == 0:
            return False

    return True


def generator():
    number = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    question = '{}'.format(number)
    if is_prime_number(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, str(correct_answer)


def prime_game():
    common_game('Answer "yes" if given number is prime. Otherwise answer "no".',
                generator)
