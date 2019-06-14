set_example = {1, 2, 2}

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)

print(unique_nums)

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)