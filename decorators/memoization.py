'''
Memoization: is an optimization technique used primarily to speed up computer programs by storing the results of expensive functions calls and returning the cached result when the same inputs occur again

The basic memoization algorithm looks as follows:

Set up a cache data structure for function results
Every time the function is called, do one of the following:
    Return the cached result, if any; or
    Call the function to compute the missing result, and then update the cache before returning the result to the caller
'''

from time import time


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result

        return result

    return memoized_func


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# benchmark 3 times with regular function --> results are the same
start = time()
print(fibonacci(35))
end = time()
print(f'func took {end - start}')

start = time()
print(fibonacci(35))
end = time()
print(f'func took {end - start}')


# benchmark 3 times with decorators --> cold to hot --> significant increase
memoized = memoize(fibonacci)

start = time()
print(memoized(35))
end = time()
print(f'func took {end - start}')

start = time()
print(memoized(35))
end = time()
print(f'func took {end - start}')
