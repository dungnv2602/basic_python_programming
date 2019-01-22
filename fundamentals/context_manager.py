# use case of context manager
from contextlib import contextmanager
import os
# How to replicate the functionality of function open()

# Method 1: Using Class


class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # Enter the runtime context related to this object. The 'with' statement will bind this method’s return value to the target(s) specified in the as clause of the statement, if any.
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be None.
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('sample.txt', 'w') as f:
    f.write('Test')

print(f.closed)

# Method 2: Using decorator
# using @contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)  # setup
        yield f  # code execute within 'with' statement
    finally:
        f.close()  # teardown▐


with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum')

print(f.closed)

# Real Application - Practical Examples
# open db & close dbconnection
# acquiring lock and releasing lock


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()  # setup
        os.chdir(destination)  # setup
        yield  # return nothing --> logic manipulation
    finally:
        os.chdir(cwd)  # teardown


with change_dir('sample-dir'):
    print(os.listdir())  # logic manipulation
