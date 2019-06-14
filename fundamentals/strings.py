m = 'Hello World'

# reverse string
m_same = m[::]
print(m_same)

m_reserved = m[::-1]
print(m_reserved)

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


# strip, lstrip, rstrip
# Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped
print('  spacious   '.strip())

print('www.example.com'.strip('cmowz. '))

print('#....... Section 3.2.1 Issue #32 .......'.strip('.#! '))


# lstrip
# Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped
print('  spacious   '.lstrip())

print('www.example.com'.lstrip('cmowz. '))

print('#....... Section 3.2.1 Issue #32 .......'.lstrip('.#! '))


# rstrip
# Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped
print('  spacious   '.rstrip())

print('www.example.com'.rstrip('cmowz. '))

print('#....... Section 3.2.1 Issue #32 .......'.rstrip('.#! '))
