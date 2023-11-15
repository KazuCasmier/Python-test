import random
import string
import time

'''
Pretty inefficient password cracker will probably optimize later
'''

password = input('Enter a password: ')

guess = ''
start = time.time()


print('your password is:', password)
print('\nPlease wait for the cracker to finish running :)')

guess_count = 0
while True:
    guess = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=len(password)))

    if guess != password:
        guess_count += 1
    elif guess == password:
        print('Guessed the password', guess, 'in', guess_count, 'attempts')
        end = time.time()
        print(end - start)
        break
