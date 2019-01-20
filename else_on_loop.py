my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)
    if i == 3:
        break
else:  # if no break is hit --> execute this code
    print('Hit the for/else statement!')

for i in my_list:
    print(i)
    if i == 6:
        break
else:  # if no break is hit --> execute this code
    print('Hit the for/else statement!')

i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print('Hit the while/else statement!')

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print('Hit the while/else statement!')


def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i


my_list = ['Dung', 'Hung', 'Phuong']
index_location = find_index(my_list, 'Hung')
print(index_location)
