import random

import prompt

from brain_games.scripts.cli import welcome_user

QUESTIONS_LIMIT = 3
OPERATION_PLUS = '+'
OPERATION_MINUS = '-'
OPERATION_MULTIPLY = '*'
OPERATIONS = [OPERATION_MINUS, OPERATION_PLUS, OPERATION_MULTIPLY]


def main():
    name = welcome_user()
    game(name)


def game(name):
    print('What is the result of the expression?')
    wrong_message = "'{first}' is wrong answer ;(. Correct answer was '{second}'."
    questions_count = 0

    while questions_count < QUESTIONS_LIMIT:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operation = OPERATIONS[random.randint(0, 2)]
        print('Question: {number1} {operation} {number2}'.format(number1=number1, number2=number2, operation=operation))
        answer_string = prompt.string('Your answer: ')
        try:
            answer = int(answer_string)
        except:
            answer = False

        correct_answer = False
        if operation == OPERATION_PLUS:
            correct_answer = number1 + number2
        elif operation == OPERATION_MINUS:
            correct_answer = number1 - number2
        elif operation == OPERATION_MULTIPLY:
            correct_answer = number1 * number2

        if answer == correct_answer:
            print('Correct!')
            questions_count += 1
        else:
            print(wrong_message.format(first=answer_string, second=correct_answer))
            print("Let's try again, {name}!".format(name=name))
            break

    if questions_count == QUESTIONS_LIMIT:
        print('Congratulations, {name}!'.format(name=name))


if __name__ == '__main__':
    main()
