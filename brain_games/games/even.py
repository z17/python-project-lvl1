import random

from brain_games.engine.game_engine import run_game

RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_round():
    number = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    question = '{number}'.format(number=number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


def even_game():
    run_game(GAME_RULES, generate_game_round)
