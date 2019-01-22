# Generators are a special class of functions that simplify the task of writing iterators. Regular functions compute a value and return it, but generators return an iterator that returns a stream of values.
# When you call a generator function, it doesn’t return a single value; instead it returns a generator object that supports the iterator protocol. On executing the yield expression, the generator outputs the value of i, similar to a return statement. The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved. On the next call to the generator’s __next__() method, the function will resume executing.
# return Generator Object - Any function containing a yield keyword is a generator function
# Generator is better performance in execution time and memory because it not holding all the values in memory
# DO NOT cast generator to list, you will lose the advantage of performance


def gen_func(nums):  # Generator Expression - similar to List Comprehension
    for n in nums:
        yield n*n


my_gen = gen_func([1, 2, 3, 4, 5])
print(my_gen)

lessons = ["Why Python Programming", "Data Types and Operators",
           "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
