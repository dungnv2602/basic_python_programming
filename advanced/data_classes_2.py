from dataclasses import dataclass, field, fields, replace, asdict, astuple, is_dataclass
from datetime import datetime
from pprint import pprint

# Be default, dataclass is not orderable --> order=True to make it orderable
# Be default, dataclass is mutable --> frozen=True to make it immutable


@dataclass(order=True, frozen=True)
class Color:
    hue: int
    saturation: float
    lightness: float = 0.5
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.hue + self.saturation + self.lightness


c = Color(33, 1.0)
print(c)  # default repr()
print(c.hue)
print(c.saturation)
print(c.lightness)

replace(c, hue=120)  # dataclass is mutable by default --> can change if specify
print(c)

print(asdict(c))

print(astuple(c))

print(Color.__annotations__)  # metadatas

colors = [Color(33, 1.0), Color(66, 0.75), Color(99, 0.5), Color(66, 0.75)]

pprint(sorted(colors))
pprint(set(colors))


@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int
    name: str
    gender: str
    salary: int = field(hash=False, repr=False, metadata={'units': 'bitcoin'})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, viewer_id):
        self.viewed_by.append((viewer_id, datetime.now()))


e1 = Employee(12312334, 'John Doe', 'male', 60000, 30)
e2 = Employee(23934982, 'John Michael', 'male', 90000, 33)

e1.access('David Tom')
e1.access('James Thumb')
e1.access('Daniel Dark')
pprint(e1.viewed_by)

pprint(sorted([e1, e2]))

assignments = {e1: 'gather requirements', e2: 'write tests'}
pprint(assignments)

pprint(Employee.__annotations__)

pprint(fields(e1)[3])


def is_dataclass_instance(obj):
    return is_dataclass(obj) and not isinstance(obj, type)
