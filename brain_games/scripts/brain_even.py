import random

import prompt

from brain_games.scripts.cli import welcome_user

QUESTIONS_LIMIT = 3


def main():
    name = welcome_user()
    game(name)


def game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wrong_message = "'{first}' is wrong answer ;(. Correct answer was '{second}'."
    questions_count = 0

    while questions_count < QUESTIONS_LIMIT:
        number = random.randint(1, 100)
        print('Question: {number}'.format(number=number))
        answer = prompt.string('Your answer: ').lower()

        correct_answer = 'yes' if number % 2 == 0 else 'no'

        if answer == correct_answer:
            print('Correct!')
            questions_count += 1
        else:
            print(wrong_message.format(first=answer, second=correct_answer))
            print("Let's try again, {name}!".format(name=name))
            break

    if questions_count == QUESTIONS_LIMIT:
        print('Congratulations, {name}!'.format(name=name))


if __name__ == '__main__':
    main()
