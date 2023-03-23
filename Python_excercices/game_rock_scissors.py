import random


def user_choice_v():
    print('You can choose from Rock, Scissors, Paper')
    user_input = input('What do you choose? ')
    return user_input


def ai_choice_v():
    choices = ['Rock', 'Scissors', 'Paper']
    choice = random.choice(choices)
    return choice


def check_result(user_choice, ai_choice):
    if user_choice == ai_choice:
        return 'Its a Draw!'
    elif user_choice == 'Rock':
        if ai_choice == 'Paper':
            return 'Ai won'
        elif ai_choice == 'Scissors':
            return 'User won'
    elif user_choice == 'Scissors':
        if ai_choice == 'Paper':
            return 'User won'
        elif ai_choice == 'Rock':
            return 'Ai won'
    elif user_choice == 'Paper':
        if ai_choice == 'Rock':
            return 'User won'
        elif ai_choice == 'Scissors':
            return 'Ai won'


def game():
    user_guess = user_choice_v()
    ai_guess = ai_choice_v()
    print(check_result(user_choice=user_guess, ai_choice=ai_guess))
    print(f'User choice was {user_guess} and computer choice was {ai_guess}')


def play_in_loop():
    play_again = ''
    answers = ['No', 'N', 'n']
    while play_again not in answers:
        game()
        play_again = input('Want to play again? ')


play_in_loop()