import prompt

QUESTIONS_LIMIT = 3

STRING_WELCOME = 'Welcome to the Brain Games!'
STRING_HELLO = 'Hello, {name}!'
STRING_WRONG_MESSAGE = "'{}' is wrong answer ;(. Correct answer was '{}'."
STRING_TRY_AGAIN = "Let's try again, {name}!"
STRING_CORRECT = 'Correct!'
STRING_CONGRATULATIONS = 'Congratulations, {name}!'
STRING_ASK_ANSWER = 'Your answer: '
STRING_QUESTION = 'Question: {}'
STRING_ASK_NAME = 'May I have your name? '


def run_game(rules, round_generator):
    print(STRING_WELCOME)
    name = prompt.string(STRING_ASK_NAME)
    print(STRING_HELLO.format(name=name))

    print(rules)
    questions_count = 0

    while questions_count < QUESTIONS_LIMIT:
        (question, correct_answer) = round_generator()
        print(STRING_QUESTION.format(question))
        answer = prompt.string(STRING_ASK_ANSWER)

        if answer.lower() == correct_answer:
            print(STRING_CORRECT)
            questions_count += 1
        else:
            print(STRING_WRONG_MESSAGE.format(answer, correct_answer))
            print(STRING_TRY_AGAIN.format(name=name))
            break
    else:
        print(STRING_CONGRATULATIONS.format(name=name))
