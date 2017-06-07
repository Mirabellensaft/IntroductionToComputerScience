
x = 100
low = 0
high = x
guess = (low + high) // 2

print('Please think of a number between 0 and 100!')
print('Is your secret number ' + str(guess) + ' ?')
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
ans = input(' ').lower()


while True:
    if ans == 'h':
        high = guess
        guess = (low + high) // 2
        print('Is your secret number ' + str(guess) + ' ?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
        ans = input(' ').lower()
    elif ans == 'l':
        low = guess
        guess = (low + high) // 2
        print('Is your secret number ' + str(guess) + ' ?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
        ans = input(' ').lower()
    elif ans == 'c':
        print('Game over. Your secret number was: ' + str(guess) + ' !')
        break
    else :
        print('You hit the wrong key, bastard!')
        print('Is your secret number ' + str(guess) + ' ?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
        ans = input(' ').lower()
