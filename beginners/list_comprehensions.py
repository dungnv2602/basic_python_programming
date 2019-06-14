cities = ['new york', 'mountain view', 'chicago', 'los angeles']
#Use list comprehension
capitalized_cities = [city.title() for city in cities]

print(capitalized_cities)

#Conditionals in List Comprehensions
squares = [x**2 for x in range(9) if x % 2 == 0]

print(squares)

squares = [x**2 if x % 2 == 0 else x+3 for x in range(9)]

print(squares)
