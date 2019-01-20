class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # getter decorator
    def email(self):  # can access method email like an attribute
        return '{}.{}@email.com'.format(self.first, self.last)

    @property  # getter decorator
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('deleter executed')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Dung Nguyen'  # using setter

print(emp_1.first)
print(emp_1.email)  # can access method email like an attribute
print(emp_1.fullname)

del emp_1.fullname  # using deleter
