import random

from brain_games.engine.game_engine import run_game

PROGRESSION_START_VALUE_MIN = 1
PROGRESSION_START_VALUE_MAX = 50

PROGRESSION_STEP_VALUE_MIN = 50
PROGRESSION_STEP_VALUE_MAX = 50

PROGRESSION_LENGTH_VALUE_MIN = 5
PROGRESSION_LENGTH_VALUE_MAX = 15

GAME_RULES = 'What number is missing in the progression?'


def generate_game_round():
    length = random.randint(PROGRESSION_LENGTH_VALUE_MIN,
                            PROGRESSION_LENGTH_VALUE_MAX)
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
    run_game(GAME_RULES, generate_game_round)
