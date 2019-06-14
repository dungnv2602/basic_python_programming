# *args : NON-KEYWORDED arguments
# *kwargs: KEYWORED arguments

# merge list
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

list3 = [*list1, *list2]
print(list3)

# merge dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict3 = {**dict1, **dict2}  # unpacking dictionaries
print(dict3)


def func(*args):  # accept variable number of arguments
    for arg in args:
        print(arg)


my_list = [11, 3, 4, 5, "tuts"]

print(func(*my_list))  # put in variable number of elements of list as arguments


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)


def print_values(**kwargs):
    for key, value in kwargs.items():  # dictionary
        print("The value of {} is {}".format(key, value))


print_values(my_name="Sammy", your_name="Casey")


def example(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
    pass
