my_set = {x for x in range(10)}  # set comprehension

my_dict = {x: x * x for x in range(5)}  # dict comprehension

cities = ['new york', 'mountain view', 'chicago', 'los angeles']
# Use list comprehension
capitalized_cities = [city.title() for city in cities]

print(capitalized_cities)

# Conditionals in List Comprehensions
squares = [x**2 for x in range(9) if x % 2 == 0]

print(squares)

squares = [x**2 if x % 2 == 0 else x+3 for x in range(9)]

print(squares)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = [(index, value) for index, value in enumerate(nums)]
print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_list = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_list)


def gen_func(nums):  # Generator Expression - similar to List Comprehension
    for n in nums:
        yield n*n


my_gen = gen_func(nums)
print(my_gen)
