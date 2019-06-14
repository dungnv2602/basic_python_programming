import pathlib

pathlib.Path.cwd()
pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt')
# A third way to construct a path is to join the parts of the path using the special operator /.
# The forward slash operator is used independently of the actual path separator on the platform
pathlib.Path.home() / 'python' / 'scripts' / 'test.py'
pathlib.Path.home().joinpath('python', 'scripts', 'test.py')  # /home/gahjelle/python/scripts/test.py

# Writing and Reading Files
path = pathlib.Path.cwd().joinpath('test.md')
with open(path, mode='r') as fid:
    headers = [line.strip() for line in fid]

with path.open(mode='r') as fid:  # same as above
    headers = [line.strip() for line in fid]

'''For simple reading and writing of files, there are a couple of convenience methods in the pathlib library:

.read_text(): open the path in text mode and return the contents as a string.
.read_bytes(): open the path in binary/bytes mode and return the contents as a bytestring.
.write_text(): open the path and write string data to it.
.write_bytes(): open the path in binary/bytes mode and write data to it.

Each of these methods handles the opening and closing of the file, making them trivial to use'''
pathlib.Path('test.md').read_text()

# The .resolve() method will find the full path
path = pathlib.Path('test.md')
path.resolve()  # PosixPath('/home/gahjelle/realpython/test.md')

'''
The different parts of a path are conveniently available as properties. Basic examples include:

.name: the file name without any directory
.parent: the directory containing the file, or the parent directory if path is a directory
.stem: the file name without the suffix
.suffix: the file extension
.anchor: the part of the path before the directories'''

path  # PosixPath('/home/gahjelle/realpython/test.md')
path.name  # 'test.md'
path.stem  # 'test'
path.suffix  # '.md'
path.parent  # PosixPath('/home/gahjelle/realpython')
path.parent.parent  # PosixPath('/home/gahjelle')
path.anchor  # '/'

# .parent returns a new Path object, whereas the other properties return strings. This means for instance that .parent can be chained as in the last example or even combined with / to create completely new paths
path.parent.parent / ('new' + path.suffix)  # PosixPath('/home/gahjelle/new.md')


str(pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt'))  # C:\\Users\\gahjelle\\realpython\\file.txt
