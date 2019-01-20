# best practice: use context manager
with open('test.txt', 'r') as f:
    for line in f:
        print(line)

with open('test.txt', 'r') as f:
    size = 100
    f_content = f.read(size)  # read 100 characters

    while len(f_content) > 0:
        print(f_content)
        f_content = f.read(size)

with open('test.txt', 'r') as f:
    f.tell()  # current position
    f.seek(0)  # move pointer to specified position: 0

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        size = 4096
        rf_content = rf.read(size)  # read 4096 characters

        while len(f_content) > 0:
            wf.write(line)
            rf_content = rf.read(size)

# reading and writing bytes: 'b'
with open('test.txt', 'rb') as rf:
    with open('test_copy.txt', 'wb') as wf:
        size = 4096
        rf_content = rf.read(size)  # read 4096 characters

        while len(f_content) > 0:
            wf.write(line)
            rf_content = rf.read(size)

