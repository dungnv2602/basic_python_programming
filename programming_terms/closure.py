# •	Closure: a closure is a record storing a function  together with an environment. The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created. Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.

# In simple term: A closure is an inner function that remembers and has access to variables in the local scope of the outer function in which it was created even after the outer function has finished executing (free variable)


def html_tag(tag):  # closure
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')  # tag is free variable
    return wrap_text


print_h1 = html_tag('h1')  # is wrap_text function
print_h1('Headline')


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def logger(func):
    def log_func(*args):
        # do logic A of THIS FUNCTION
        print(f'Running "{func.__name__}" with arguments {args}')

        rs = func(*args)  # do logic B of FREE VARIABLE FUNCTION
        print(rs)
    return log_func


add_logger = logger(add)  # is log_func function
sub_logger = logger(sub)  # is log_func function

add_logger(5, 4)
sub_logger(5, 4)
