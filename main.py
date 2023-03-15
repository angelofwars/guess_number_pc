import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f'Guess a number between 1 and {x}: ')
        if int(guess) < random_number:
            print('Sorry, guess again. Too low.')
        elif int(guess) > random_number:
            print('Sorry, guess again. Too high')
        else:
            print(f'Yay, congats. You have guessed the number {random_number} correctly!!!')
            exit()


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high, (H), too low (L), or correct (C)???').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Да ты выйграл ваш номер {guess}')

computer_guess(10)
