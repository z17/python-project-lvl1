import math
import random

from brain_games.engine.game_engine import run_game

RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 500

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    if number <= 1:
        return False

    middle = int(math.ceil(number / 2) + 1)
    for i in range(2, middle):
        if number % i == 0:
            return False

    return True


def generate_game_round():
    number = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    question = '{}'.format(number)
    if is_prime_number(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, str(correct_answer)


def prime_game():
    run_game(GAME_RULES, generate_game_round)
