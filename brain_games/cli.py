import prompt

def greet(text=None):
    print('Welcome to the Brain Games!')
    print(text)
    name = prompt.string('\nMay I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask(text):
    response = prompt.string(
        f'{text}\n' \
        f'Your answer: ')
    return response

def run(game):
    name = greet(game.DESCRIPTION)
    correct_answers_counter = 0

    for a in range(game.ATTEMPTS):
        question, answer = game.stage()
        user_answer = ask(question)
        if str(answer) == user_answer:
            correct_answers_counter += 1
            print(f'Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. " \
                f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    
    if correct_answers_counter == game.ATTEMPTS:
        print(f'Congratulations, {name}!')