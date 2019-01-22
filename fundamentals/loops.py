nums = [1, 2, 3, 4, 5]

# break, continue
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# nested loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

# loop in certain time
for i in range(10):
    print(i)

# while loop
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

while True:
    if x == 5:
        break
    print(x)
    x += 1
