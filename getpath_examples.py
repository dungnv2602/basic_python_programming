import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file abs path")
abs_path = os.path.abspath(__file__)
print(abs_path + "\n")

print("This file directory only")
print(os.path.dirname(full_path)+"\n")
print(os.path.dirname(__file__)+"\n")
print(os.path.abspath(os.path.dirname(__file__))+"\n")

print("Join path: ")
basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(basedir, 'restaurantmenu.db'))
