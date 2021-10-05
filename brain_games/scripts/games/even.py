import random

from brain_games.scripts.games.common_game import common_game


def generator():
    number = random.randint(1, 100)
    question = 'Question: {number}'.format(number=number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


def even_game():
    common_game('Answer "yes" if the number is even, otherwise answer "no".', generator)
