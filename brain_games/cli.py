import prompt

def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('\nMay I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask(text):
    response = prompt.string(
        f'{text}\n' \
        f'Your answer: ')
    return response
