import math
import random

from brain_games.games.common_game import common_game

RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def generator():
    number1 = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    number2 = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    question = '{} {}'.format(number1, number2)
    correct_answer = math.gcd(number1, number2)
    return question, str(correct_answer)


def gcd_game():
    common_game('Find the greatest common divisor of given numbers.', generator)
