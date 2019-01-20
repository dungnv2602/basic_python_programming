import datetime


class Employee:  # a class is a blueprint for creating instances
    # Attribute: data associated with a specific class
    # Method: function associated with a specific class

    raise_amount = 1.04  # class variable: contains data that is the same to each instance

    # a dunder method, a initialize method or constructor, is implicitly called when creating objects
    def __init__(self, first, last, pay):
        # instance variable: contains data that is unique to each instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    # regular method --> receives the instance 'self' as the first argument automatically --> need to specify to separate with static method
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # we should   access class variable through the class
        self.pay = int(self.pay * Employee.raise_amount)

    # class method --> receives the class 'cls' as the first argument automatically

    @classmethod  # decorator @classmethod: alter the functionality of a method to become class method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # decorator @staticmethod: alter the functionality of a method to become static method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.14

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.44

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        """ printout all employees

        Keyword arguments:
        self - - instance pass
        Return: all employees
         """

        for emp in self.employees:
            print('-->', emp.fullname())


# instance 'emp_1' is passed as the first argument automatically
emp_1 = Employee('Dung', 'Nguyen', 50000)
# instance 'emp_2' is passed as the first argument automatically
emp_2 = Employee('Dung', 'Nguyen', 60000)

print(emp_1.fullname())  # instance 'emp_1' is passed as argument automatically
print(Employee.fullname(emp_1))  # have the same functionality as above

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)

new_emp = Employee.from_string('Dung-Nguyen-70000')


my_date = datetime.date(2019, 7, 10)
print(Employee.is_workday(my_date))

dev_1 = Developer('Dung', 'Nguyen', 50000, 'python')
dev_2 = Developer('Hung', 'Nguyen', 50000, 'java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_2])

print(isinstance(mgr_1, Employee))
print(issubclass(Manager, Employee))
