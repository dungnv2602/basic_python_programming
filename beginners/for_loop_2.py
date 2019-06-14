names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    name = name.lower().replace(' ','_')
    usernames.append(name)

print(usernames)

for index in range(len(names)):
    names[index] = names[index].lower().replace(' ','_')

print(names)