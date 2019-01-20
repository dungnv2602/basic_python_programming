# •	Memoization: is an optimization technique used primarily to speed up computer programs by storing the results of expensive functions calls and returning the cached result when the same inputs occur again

import time

ef_cache = {}


def expensive_func(num):
    if num in ef_cache:  # if input is already occur before --> return value from dict
        return ef_cache[num]

    print "Computing {}...".format(num)
    time.sleep(1)
    result = num*num
    ef_cache[num] = result  # add value to dict to remember value of input
    return result


result = expensive_func(4)
print result

result = expensive_func(10)
print result

result = expensive_func(4)
print result

result = expensive_func(10)
print result
