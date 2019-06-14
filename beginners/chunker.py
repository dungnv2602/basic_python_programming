def chunker(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]


for chunk in chunker(range(25), 4):
    print(list(chunk))

