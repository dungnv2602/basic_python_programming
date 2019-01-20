student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['courses'])

# get value
rs = student.get('phone', 'Not Found')
print(rs)

# add or update
student['name'] = 'John'
student['phone'] = '555-555-5555'

# update entire dict
student.update({'name': 'Dung', 'age': 25, 'phone': '123-456-7890',
                'courses': ['Math', 'CompSci']})
print(student)

# delete key-value
del student['age']
print(student)

# pop last key-value
rs = student.pop()
print(rs)

# length key
print(len(student))

# all keys
print(student.keys())

# all values
print(student.values())

# key-value pairs
print(student.items())

# loop
for key, value in student.items():
    print('Key: {}, Value: '.format(key, value))