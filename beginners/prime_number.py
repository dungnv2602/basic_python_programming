## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for number in check_prime:
    if number % 2 != 0 and number % 5 != 0 and number % 3 != 0:
        print("{} is a prime number.".format(number))
    else:
        print("{} is not a prime number.".format(number))
        if number % 2 == 0:
            print("{} is a factor of {}".format(2, number))
        elif number % 3 == 0:
            print("{} is a factor of {}".format(3, number))
        elif number % 5 == 0:
            print("{} is a factor of {}".format(5, number))