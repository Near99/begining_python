number = 23
guess = int(input('enter an integer : '))

if guess == number:
    # new block starts here
    print('congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # new block ends here
elif guess < number:
    # another block
    print('no, it is a little highter than that')
    # you can do whatever you want in a block..
else:
    print('no, it is a little lower than that')
    # you must have guessed > number to reach here

print('done')
# this last statement is always executed,
# after the if statement is executed.
