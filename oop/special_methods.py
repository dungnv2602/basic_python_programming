class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Dung', 'Nguyen', 50000)
emp_2 = Employee('Hung', 'Nguyen', 60000)

print(emp_1)  # refer call __str__ method
print(str(emp_1))  # refer call __str__ method
print(emp_1.__str__())  # directly call __str__ method

print(repr(emp_1))  # refer call __repr__ method
print(emp_1.__repr__())  # directly call __repr__ method

print(emp_1+emp_2)  # refer call __add__ method

print(len(emp_1))
