age = 20
name= 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
#fill with underscores (_) with the text centerd
#(^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
#keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
#specify a two line string (\n)
print('This is the first line\nThis is the second line')

print('This is the first sentence.\
       This is the secound sentence'r"newlines are indicated by \n")

print(r"newlines are indicated by \n")
