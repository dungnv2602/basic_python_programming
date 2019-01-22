# if-else
# and or not
# Object Identity 'is'

# False Values:
# False
# None
# Zero of any numeric type (!= 0 --> True)
# Any empty sequence. E.g: '', (), [] (empty string, tuple, list) (>< not empty -> True)
# Any empty mapping. E.g: {} (empty dict) (>< not empty -> True)
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
elif user == 'Admin' or logged_in:
    print('OR')
elif not logged_in:
    print('NOT')
else:
    print('Bad Creds')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # check whether the value of a and b is the same

print(a is b)  # check whether the id of a and b is the same
print(id(a))
print(id(b))
