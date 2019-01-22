m = 'Hello World'

# count number of character
print(m.count('l'))

# find the index start at
print(m.find('l'))

# replace string -> return new string
new_m = m.replace('World', 'Universe')

# format string
m = '{}, {}. Welcome!'.format('Hello', 'Dung')

# f string
greeting = 'Hello'
name = 'Michael'
m = f'{greeting}, {name.upper()}. Welcome!'
print(m)

# dir(), help()
print(dir(name))
print(help(str))
print(help(str.lower))