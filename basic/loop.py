secret_number = 9
guess_count = 0
max_guess = 3
while guess_count < max_guess:
    guess = int(input('guess: '))
    guess_count = guess_count+1
    if guess == secret_number:
        print('you win')
        break
    else:
        print('wrong')
    print('game over')