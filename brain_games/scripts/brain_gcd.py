import random

import math

from brain_games.scripts.games.common_game import common_game


def main():
    game()


def generator():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = 'Question: {} {}'.format(number1, number2)
    correct_answer = math.gcd(number1, number2)
    return question, str(correct_answer)


def game():
    common_game('Find the greatest common divisor of given numbers.', generator)


if __name__ == '__main__':
    main()
