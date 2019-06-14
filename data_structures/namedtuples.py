'''
First of all, namedtuples are immutable just like regular tuples. Once you store something in them you can’t modify it.

Besides that, namedtuples are, well…named tuples. Each object stored in them can be accessed through a unique (human-readable) identifier. This frees you from having to remember integer indexes, or resorting to workarounds like defining integer constants as mnemonics for your indexes.

A good way to view them is to think that namedtuples are a memory-efficient shortcut to defining an immutable class in Python manually.
'''


from collections import namedtuple
import json


Car = namedtuple('Car', ['color', 'mileage'])
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

my_car = Car('red', 3812.4)
my_electric_car = ElectricCar('red', 1234.5, 45.0)

# exact
print(my_car.color)
print(my_car.mileage)
print(*my_car)
print(my_car[0])

# unpack
color, mileage = my_car
print(color, mileage)
print(tuple(my_car))

# string representation
print(my_car)
print(my_electric_car)

# built-in helper methods
print(my_electric_car._fields)  # generate fields
# generate ordered dict
print(my_electric_car._asdict())
print(json.dumps(my_electric_car._asdict()))
# replace data
modified_car = my_car._replace(color='blue')
print(modified_car)
# _make() classmethod can be used to create new instances of a namedtuple from a sequence or iterable:
new_car1 = ['red', 999]
new_car1 = Car._make(new_car1)
print(new_car1)
