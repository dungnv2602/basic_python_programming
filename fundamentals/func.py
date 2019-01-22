# function - black box: focus on the input and output, don't need to know what doing inside


def student_info(*args, **kwargs):  # *:list; **:dict
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
infos = {'name': 'Dung', 'age': 24}

student_info(*courses, **infos)

import datetime
import calendar
import os

today = datetime.date.today()

calendar.isleap(2017)

os.getcwd()

os.environ.get('PATH')

os.__name__

__file__
