# In general, list and tuple are the same in functionality
# but list is mutable and tuple is immutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']  # mutable
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')  # immutable
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

