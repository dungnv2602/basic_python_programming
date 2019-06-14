limit = 40
number = 2
nearest_square = 0
# write your while loop here
while number**2 < limit:
    nearest_square = number**2
    number += 1

print(nearest_square)