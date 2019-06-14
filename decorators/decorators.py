# decorator: a function that take another function as an argument
# practical examples: logging, execution time, v.vv
# way 1: decorator function --> more prefer


import time
from functools import wraps


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('executed before', original_function.__name__)
        result = original_function(*args, **kwargs)
        print('executed after', original_function.__name__)
        return result
    return wrapper_function

# way 2: decorator class


class decorator_class(object):  # just another decorator option
    def __init__(self, original_function):
        # tie the original_function with the instance variable of this class
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('__call__ method executed')
        return self.original_function(*args, **kwargs)


# @decorator_function -->equal to display = decorator_function(display)
@decorator_class  # just another decorator option
def display():
    print('display function ran')


# @decorator_function
@decorator_class  # just another decorator option
def display_info(name, age):
    print(f'display_info function ran with {name} and {age}')


"""display = decorator_function(display) --> display()"""
display()  # same as above
display_info('Dung', 23)

# decorating methods


def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family


# Decorators


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)  # decorate wrapper function with wraps decorator
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)  # decorate wrapper function with wraps decorator
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

# apply multiple decorators


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


# equal --> display_info = my_logger(my_timer(display_info))
display_info('Tom', 22)

# decorator accept arguments


def prefix_decorator(prefix):
    def decorator_function(original_function):
        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            print(prefix, 'executed before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'executed after', original_function.__name__)
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


def tags(tag_name):
    def tags_decorator(func):
        # in case of debugging that can be problematic since the wrapper function does not carry the name, module and docstring of the original function
        # Wraps is a decorator for updating the attributes of the wrapping function(func_wrapper) to those of the original function(get_text). This is as simple as decorating func_wrapper by @wraps(func).
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name


print(get_text.__name__)  # get_text
print(get_text.__doc__)  # returns some text
print(get_text.__module__)  # __main__
