#Define a dictionary
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary

print(elements["helium"])  # print the value mapped to "helium"

x = elements["helium"]

print(x)

#x = elements["none"] #KeyError: 'none'

x = elements.get('none')

if x is not None:
    print(x)
else:
    print('Key not found')

elements = {'Shanghai':17.8, 'Isanbul':13.3, 'Karachi': 13.0, 'Mumbai':12.5}