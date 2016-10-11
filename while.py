number = 23
running = True #1

while running:
    guess = int(input('enter an integer : '))

    if guess == number:
        print('congratulations')
        running = False #0
    elif guess < number:
        print('no, it is a little higher')
    else:
        print('no, it is a little lower')
else:
    print('the while loop is over.')

print ('done')
