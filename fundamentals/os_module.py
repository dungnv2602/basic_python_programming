import os
from datetime import datetime

# current dir
print(os.getcwd())

# change dir
os.chdir('D:/')

# list dir
os.listdir()

# create dir
os.mkdir('new_dir')  # cannot create tree structure
os.makedirs('new_dir/sub_dir')  # can create tree structure

# remove dir
os.rmdir('sub_dir')
os.removedirs('new_dir/sub_dir')

# rename
os.rename('demo.txt', 'demo_updated.txt')

# file stat
os.stat('demo.txt')
last_modified_time = os.stat('demo.txt').st_mtime
datetime.fromtimestamp(last_modified_time)

# walk()
for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('Current path: ', dirpath)
    print('Directory: ', dirname)
    print('Files: ', filename)

# env variables
home = os.environ.get('HOME')
filepath = os.path.join(home, 'test.txt')

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
