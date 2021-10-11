import random

from brain_games.scripts.games.common_game import common_game

PROGRESSION_START_VALUE_MIN = 1
PROGRESSION_START_VALUE_MAX = 50

PROGRESSION_STEP_VALUE_MIN = 50
PROGRESSION_STEP_VALUE_MAX = 50

PROGRESSION_LENGTH_VALUE_MIN = 5
PROGRESSION_LENGTH_VALUE_MAX = 15


def generator():
    length = random.randint(PROGRESSION_LENGTH_VALUE_MIN, PROGRESSION_LENGTH_VALUE_MAX)
    step = random.randint(PROGRESSION_STEP_VALUE_MIN,
                          PROGRESSION_STEP_VALUE_MAX)
    start = random.randint(PROGRESSION_START_VALUE_MIN,
                           PROGRESSION_START_VALUE_MAX)
    skip_index = random.randint(0, length - 1)

    progression = []
    for i in range(start, start + (length * step), step):
        progression.append(str(i))

    correct_answer = progression[skip_index]
    progression[skip_index] = '..'
    sequence = " ".join(progression)
    question = '{}'.format(sequence)
    return question, str(correct_answer)


def progression_game():
    common_game('What number is missing in the progression?', generator)
