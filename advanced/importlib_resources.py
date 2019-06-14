from importlib import resources

# importlib.resources.read_binary(package, resource): Read and return the contents of the resource within package as bytes.

'''importlib.resources.read_binary(package, resource): Read and return the contents of the resource within package as bytes.
package is either a name or a module object which conforms to the Package requirements. resource is the name of the resource to open within package;
it may not contain path separators and it may not have sub-resources (i.e. it cannot be a directory). This function returns the contents of the resource as bytes.'''
contents = resources.read_binary('advanced', 'file.txt')
contents = resources.read_binary('advanced.subdir', 'sub_file.txt')


contents = resources.read_text('advanced', 'file.txt')
contents = resources.read_text('advanced.subdir', 'sub_file.txt')

with resources.open_binary("advanced.subdir", "sub_file.txt") as fid:
    contents = fid.readlines()

with resources.open_text("advanced.subdir", "sub_file.txt") as fid:
    contents = fid.readlines()
