# Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors. The goal of using assertions is to let developers find the likely root cause of a bug more quickly. An assertion error should never be raised unless there’s a bug in your program.


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    # It will guarantee that, no matter what, discounted prices cannot be lower than $0 and they cannot be higher than the original price of the product.
    assert 0 <= price <= product['price']
    return price
