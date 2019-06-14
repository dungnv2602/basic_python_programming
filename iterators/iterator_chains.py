def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


# This is what our “data pipeline” or “chain of generators” would do
chain = negated(squared(integers()))

# Chained Generator Expression
squared = (i*i for i in range(1, 9))
negated = (-i for i in squared)
