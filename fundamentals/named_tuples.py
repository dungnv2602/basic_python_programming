# similar to regular tuple but ore readable
# provide more readability but keep the functionality of a tuple: immutable

from collections import namedtuple

# regular tuple
color = (55, 155, 255)  # immutable
print('Regular tuple: ', color[0])
# --> lack information
# maybe switch to dictionary for more concise information
color = {'red': 55, 'green': 155, 'blue': 255}  # mutable
print('Dict: ', color['red'])
# --> color supposed to be immutable
# --> switch to namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)
white = Color(255, 255, 255)

print(color[0])
print(color.red)
