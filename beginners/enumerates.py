cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
enumerated = enumerate(cast)
for index, name in enumerate(cast):
    name+=' {}'.format(heights[index])
    cast[index] = name

print(cast)