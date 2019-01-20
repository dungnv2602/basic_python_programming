
# o	An immutable object is an object whose state cannot be modified after it is created
# o	A mutable object is an object whose state can be modified after it is created

# Efficiently concat string
strs = ['Nguyen', 'Viet', 'Dung', 'Fullstack', 'Web', 'Developer']


joined = ' '.join(strs)

print(joined)

joined = ' '.join([str(x) for x in range(10)])

print(joined)


def order_statistic(my_list, num, is_reversed=False):
    my_list.sort(reverse=is_reversed)
    return my_list[:num]

my_list = [1, 6, 7, 4, 2, 7, 3, 7, 2, 8, 3, 2]

rs = order_statistic(my_list, 3, True)

print(rs)
