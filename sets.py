# Set
set_courses_1 = {'History', 'Math', 'Physics', 'CompSci'}
set_courses_2 = {'History', 'Math', 'Art', 'Design'}

# add, update
s1 = {1, 2, 3, 4, 5}
s1.add(6)
s1.update([7, 8, 9])
s2 = {10, 11, 12}
s1.update(s2, [13, 14, 15])

# remove
s1.remove(5)  # throw error if key doesn't exist
s1.discard(5)  # do not throw error if key doesn't exist
s1.pop()


# membership test
print('Math' in set_courses_1)

# check values exist in set_courses_1 and set_courses_2
print(set_courses_1.intersection(set_courses_2))

# check value in set_courses_1 but not in set_courses_2
print(set_courses_1.difference(set_courses_2))

# check values in set_courses_1 but not in set_courses_2 and vice versa
print(set_courses_1.symmetric_difference(set_courses_2))

# union
print(set_courses_1.union(set_courses_2))

# empty set
empty_set = set()

l1 = [1, 2, 3, 1, 2, 3]

l2 = list(set(l1))

# membership test of list --> convert to set to check
is_exist = 1 in set(l1)
print(is_exist)
