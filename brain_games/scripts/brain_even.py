from brain_games.cli import greet
from brain_games.cli import ask


questions = [
    [15, 'no'],
    [6, 'yes'],
    [7, 'no']
]


def main():
    name = greet()
    correct_answers_counter = 0

    for q in questions:
        question = q[0]
        correct_answer = q[1]

        answer = ask(f'Question: {question}')
        if answer in correct_answer:
            correct_answers_counter += 1
            print(f'Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            exit()

    if correct_answers_counter == len(questions):
        print(f'Congratulations, {name}!')
    else:
        print(f'{correct_answers_counter}')

if __name__ == '__main__':
    main()