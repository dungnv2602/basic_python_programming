# Just like list comprehensions, generators can also be written in the same manner except they return a generator object rather than a list
from collections import namedtuple


my_list = ['a', 'b', 'c', 'd']

lists = [x for x in my_list]  # list comprehension

for x in lists:  # loop value from a LIST
    print(x)

gen_objs = (x for x in my_list)  # generator expression

for x in gen_objs:  # loop value from a GENERATOR OBJECT
    print(x)


Scientist = namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])  # immutable

# whole data is immutable --> important in functional programming
scientists = (
    Scientist('Marie Curie', 'physics', 1867, True),
    Scientist('Lance Curie', 'math', 1811, False),
    Scientist('Marie Yuan', 'chemistry', 1702, True),
    Scientist('YuYu Hakusho', 'biochemistry', 1666, False),
    Scientist('Fukujama Rei', 'physics', 1111, True),
    Scientist('Donald Duck', 'math', 2010, False)
)

nobeled_scientists = tuple(s for s in scientists if s.nobel)  # generator expression
print(nobeled_scientists)

names_and_ages = tuple((s.name, s.born) for s in scientists)  # generator expression
print(names_and_ages)
