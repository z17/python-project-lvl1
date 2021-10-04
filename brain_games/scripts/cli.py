import prompt


def get_name():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name
