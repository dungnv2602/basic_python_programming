x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
zipped = zip(labels, x_coord, y_coord, z_coord)

for label, x, y, z in zipped:
    points.append('{}: {}, {}, {}'.format(label, x, y, z))

for point in points:
    print(point)

# Zip List to Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}
zipped = zip(cast_names, cast_heights)
for name, height in zipped:
    cast[name] = height

print(cast)

# Unzip Tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72),
        ("Lily", 66), ("Marshall", 76))
# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)

# Transpose with Zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)
