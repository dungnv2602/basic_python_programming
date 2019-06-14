# An immutable version of set that cannot be changed after it was constructed. Frozensets are static and only allow query operations on their elements (no inserts or deletions.) Because frozensets are static and hashable they can be used as dictionary keys or as elements of another set.
from collections import Counter
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})

'''
The collections.Counter class in the Python standard library implements a multiset (or bag) type that allows elements in the set to have more than one occurrence.

This is useful if you need to keep track not only if an element is part of a set but also how many times it is included in the set.'''

inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)

more_loot = {'sword': 1, 'apple': 1, 'bread': 1}
inventory.update(more_loot)
print(inventory)

# get length
print(sum(inventory.values())
