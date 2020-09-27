import os
import random

def print_header_line(width):
    for x in range(width):
        print('-',end='')
    next
    print()
ds = 72
print_header_line(ds)
print('                          Y o u  G u e s s   ')
print_header_line(ds)
print('Running On:')
print(os.sys.version)
print_header_line(ds)
guess = -1
nog = 0
low = 1
high = 100
secret = random.randint(low,high)

print_header_line(ds)
while guess != secret :
    nog = nog + 1
    guess_text = input('Please Enter a Number between {} and {} :'.format(low,high))
    guess = int(guess_text)
    if guess > secret :
        print('{} is too high '.format(guess))
    elif guess < secret :
        print('{} is too low '.format(guess))
    else :
        print('You got it in {} guesses'.format(nog))

print_header_line(ds)
print('Done')
