f = open('config_path.txt', 'r')

file_data = f.read()

f.close()

print(file_data)

f = open('file_demo.txt', 'w')
f.write('Hello World')
f.close()

list_data = []

with open('config_path.txt', 'r') as f:
    list_data = f.readlines()

list_data.clear()

with open('config_path.txt', 'r') as f:
    for line in f:
        list_data.append(line.strip())

print(list_data)
