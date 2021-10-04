import prompt

from brain_games.scripts.cli import get_name

QUESTIONS_LIMIT = 3


def common_game(rules, generator):
    name = get_name()
    print(rules)
    wrong_message = "'{first}' is wrong answer ;(. Correct answer was '{second}'."
    questions_count = 0

    while questions_count < QUESTIONS_LIMIT:
        (question, correct_answer) = generator()
        print(question)
        answer = prompt.string('Your answer: ')

        if answer.lower() == correct_answer:
            print('Correct!')
            questions_count += 1
        else:
            print(wrong_message.format(first=answer, second=correct_answer))
            print("Let's try again, {name}!".format(name=name))
            break

    if questions_count == QUESTIONS_LIMIT:
        print('Congratulations, {name}!'.format(name=name))
