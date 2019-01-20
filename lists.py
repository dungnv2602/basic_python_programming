# list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(courses[0])
print(courses[-1])
print(courses[0:2])  # [starting point - inclusive: stoping point - exclusive]
print(courses[:2])  # = above
print(courses[2:])  # [2:last index]
# len()
print(len(courses))

# add item
courses.append('Art')
print(courses)

# add index
courses.insert(0, 'Literature')
print(courses)

# add list values - extent()
courses_2 = ['English', 'Education']
courses.extend(courses_2)
print(courses)

# remove()
courses.remove('Math')

# remove last value - return value
popped = courses.pop()
print(popped)
print(courses)

# sort()
courses.reverse()
courses.sort()

nums = [1, 4, 7, 3, 9, 2]
nums.sort(reversed=True)
print(nums)

sorted_nums = sorted(nums)
print(sorted_nums)

# min, max, sum
min(nums)
max(nums)
sum(nums)

# find index of value
print(courses.index('CompSci'))

# check if value exist
print('CompSci' in courses)

# print items
for item in courses:
    print(item)

# index and value
enum = enumerate(courses, start=1)
for index, course in enum:
    print(index, course)

# turn list into string
courses_str = ', '.join(course)
print(courses_str)

# turn back to list
new_courses = courses_str.split(', ')
print(new_courses)
