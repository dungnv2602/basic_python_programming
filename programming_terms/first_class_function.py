# •	First-class function: A programming language is said to have First-class functions when functions in that language are treated like any other variable.
# assign function to a variable
# return function from a function


def square(x):
    return x * x


f = square

print(square)
print(f(5))


def logger(msg):  # closure
    def log_msg():
        print('Log:', msg)  # msg is free variable
    return log_msg


log_hi = logger('Hi!')  # is log_msg function
log_hi()


def html_tag(tag):  # closure
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')  # tag is free variable
    return wrap_text


print_h1 = html_tag('h1')  # is wrap_text function
print_h1('Headline')
