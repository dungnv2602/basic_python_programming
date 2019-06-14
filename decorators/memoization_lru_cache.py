'''
Memoization: is an optimization technique used primarily to speed up computer programs by storing the results of expensive functions calls and returning the cached result when the same inputs occur again

The basic memoization algorithm looks as follows:

Set up a cache data structure for function results
Every time the function is called, do one of the following:
    Return the cached result, if any; or
    Call the function to compute the missing result, and then update the cache before returning the result to the caller
'''

from time import time
from functools import lru_cache

'''
In general, Python’s memoization implementation provided by  functools.lru_cache is much more comprehensive than our ad hoc memoize function
'''


@lru_cache(maxsize=128)  # define the limit size of cache
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time()
print(fibonacci(35))
end = time()
print(f'func took {end - start}')

start = time()
print(fibonacci(35))
end = time()
print(f'func took {end - start}')

print(fibonacci.cache_info())

fibonacci.cache_clear()
