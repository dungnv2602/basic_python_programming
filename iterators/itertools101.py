import itertools  # The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. This means that the functions in itertools “operate” on iterators to produce more complex iterators.

import operator


def print_iterator(gen_obj):
    print(list(gen_obj))


def print_counter(counter):
    print(next(counter))
    print(next(counter))
    print(next(counter))


counter = itertools.count(start=5, step=-2.5)  # count indefinitely

print_counter(counter)

data = [100, 200]

daily_data = zip(itertools.count(), data)

print_iterator(daily_data)

daily_data = zip(itertools.zip_longest(range(10), data))

print_iterator(daily_data)


counter = itertools.cycle(['On', 'Off'])  # loop indefinitely

print_counter(counter)

counter = itertools.repeat(2)  # repeat indefinitely

print_counter(counter)

squares = map(pow, range(10), itertools.repeat(2))

print_iterator(squares)

# Make an iterator that computes the function using arguments obtained from the iterable. Used instead of map() when argument parameters are already grouped in tuples from a single iterable (the data has been “pre-zipped”).
# multiply in tutples with first to second
squares = itertools.starmap(pow, [(0, 2), (1, 3), (2, 4), (3, 3)])

print_iterator(squares)

# combination vs permutation: don't repeat values
# combination: order doesn't matter
# permutaion: order does matter

letters = ['a', 'b', 'c', 'd']
numbers = [1, 4, 6, 4, 1]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2)
print_iterator(result)

result = itertools.permutations(letters, 2)
print_iterator(result)

# Cartesian product of input iterables. Equivalent to nested for-loops.
result = itertools.product(letters, repeat=2)
print_iterator(result)

result = itertools.combinations_with_replacement(letters, 2)
print_iterator(result)

result = itertools.chain(letters, numbers, names)
print_iterator(result)

# you can't use bracket slicing or addition with iterators --> use itertools.islice()
result = itertools.islice(range(10), 1, 7, 2)
print_iterator(result)

selectors = [True, False, False, True]
result = itertools.compress(letters, selectors)
print_iterator(result)

result = itertools.compress('ABCDEF', [1, 0, 1, 0, 1, 1])
print_iterator(result)

result = filter(lambda x: x < 2, numbers)
print_iterator(result)

result = itertools.filterfalse(lambda x: x < 2, numbers)
print_iterator(result)

# seq[n], seq[n+1], starting when pred fails
result = itertools.dropwhile(lambda x: x < 5, numbers)
print_iterator(result)

# seq[0], seq[1], until pred fails
result = itertools.takewhile(lambda x: x < 5, numbers)
print_iterator(result)

# Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument). If func is supplied, it should be a function of two arguments. Elements of the input iterable may be any addable type including Decimal or Fraction.
result = itertools.accumulate([1, 2, 3, 4, 5])  # 1 3 6 10 15
print_iterator(result)

operator.mul(2, 5)  # take 2 arguments and multiples them

result = itertools.accumulate([1, 2, 3, 4, 5], operator.mul)  # 1 3 6 10 15
print_iterator(result)

# compare min in 2 values
print(list(itertools.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min)))

# compare max in 2 values
print(list(itertools.accumulate([9, 21, 17, 5, 11, 12, 2, 6], max)))

# apply lambda funtion in 2 values
print(list(itertools.accumulate([1, 2, 3, 4, 5], lambda x, y: (x + y) / 2)))

# order does matter
print(list(itertools.accumulate([1, 2, 3, 4, 5], lambda x, y: x - y)))
print(list(itertools.accumulate([1, 2, 3, 4, 5], lambda x, y: y - x)))

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]
# Make an iterator that returns consecutive keys and groups from the iterable. The key is a function computing a key value for each element.
# Generally, the iterable needs to already be sorted on the same key function.
result = itertools.groupby(people, lambda p: p.get(
    'state'))  # people is already sorted
print_iterator(result)

# The tee() function can be used to create any number of independent iterators from a single iterable. It takes two arguments: the first is an iterable inputs, and the second is the number n of independent iterators over inputs to return (by default, n is set to 2). The iterators are returned in a tuple of length n.
iterator1, iterator2 = itertools.tee(numbers)
iterator1, iterator2, iterator3, iterator4 = itertools.tee(numbers, 4)
