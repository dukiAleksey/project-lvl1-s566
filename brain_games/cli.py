import prompt


def greet(text=None):
    print('Welcome to the Brain Games!')
    if text is not None:
        print(text)
    name = prompt.string('\nMay I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask(text):
    response = prompt.string(
        f'{text}\n'
        'Your answer: ')
    return response


def run(game):
    name = greet(game.DESCRIPTION)

    for a in range(game.ATTEMPTS):
        question, answer = game.stage()
        user_answer = ask(question)
        if answer == user_answer:
            print(f'Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
