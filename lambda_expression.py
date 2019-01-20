def multiply(x, y):
    return x * y


# Use lambda
def multipply_lambda(x, y): return x * y


double = multipply_lambda(4, 7)
print(double)

# Lambda with map
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]


def mean(num_list):
    return sum(num_list)/len(num_list)


# map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable.
averages = list(map(mean, numbers))

averages = list(map(lambda x: sum(x)/len(x), numbers))


print(averages)

# Lambda with fitler
cities = ["New York City", "Los Angeles",
          "Chicago", "Mountain View", "Denver", "Boston"]


def is_short(name):
    return len(name) < 10


short_cities = list(filter(is_short, cities))

short_cities = list(filter(lambda x: len(x) < 10, cities))

print(short_cities)
