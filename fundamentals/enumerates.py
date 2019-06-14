'''
enumerate() allows you to loop over a collection of items while keeping track of the current item’s index in a counter variable.

enumerate is implemented as a Python iterator. This means that element indexes are generated lazily (one by one, just-in-time), which keeps memory use low and keeps this construct so fa
'''


names = ['Bob', 'Alice', 'Guido']

for index, value in enumerate(names):
    print(f'{index}: {value}')

for index, value in enumerate(names, 1):
    print(f'{index}: {value}')
