import random

from brain_games.scripts.games.common_game import common_game


def generator():
    length = random.randint(5, 15)
    step = random.randint(1, 10)
    start = random.randint(1, 50)
    skip_index = random.randint(0, length - 1)

    progression = []
    for i in range(start, start + (length * step), step):
        progression.append(str(i))

    correct_answer = progression[skip_index]
    progression[skip_index] = '..'
    sequence = " ".join(progression)
    question = 'Question: {}'.format(sequence)
    return question, str(correct_answer)


def progression_game():
    common_game('What number is missing in the progression?', generator)
