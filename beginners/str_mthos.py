full_name = 'Nguyen viet Dung'
print(full_name.islower())
full_name = full_name.lower()
print(full_name.islower())
print(full_name.count('u'))
print(full_name.find('t'))

#Use of format()
str1 = "dog"
print("Mohammed has {} balloons. Does your {} {}?".format(27, str1, 'bite'))

#Use of split()
#This function or method returns a data container called a list that contains the words from the input string
new_str = 'The cow jumped over the moon.'
list1 = new_str.split()
print(list1)

#Here the separator is space, and the maxsplit argument is set to 4.
list1 = new_str.split(' ', 4)
print(list1)

list1 = new_str.split('.')
print(list1)

list1 = new_str.split()
print(list1)

list1 = new_str.split(None,3)
print(list1)