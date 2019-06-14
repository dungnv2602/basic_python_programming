import csv
from collections import Counter
from itertools import zip_longest
from string import ascii_lowercase
numbers = [1, 2, 3, 4]

# all vs any
print(any(numbers))  # == not all
print(all(numbers))  # == not any

condition = any(n > 1 for n in numbers)
print(condition)


def is_prime(number):
    'return all(number % n != 0 for n in range(2, number))'
    return not any(number % n == 0 for n in range(2, number))


words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}


def translate(spanish_sentence):
    '''Return a translated version of a given sentence'''
    return ' '.join(words[spanish_word] for spanish_word in spanish_sentence.split())


# dict comprehension
letters = {letter: count for count, letter in enumerate(ascii_lowercase, start=1)}


def get_vowel_names(names):
    '''Return a list containing all names given that start with a vowel.'''
    return [name for name in names if name[0].upper() in 'UEOAI']


matrix = [[1, 2, 3], [-4, 5, -7], [5, 6, -2]]


def flatten(matrix):
    '''Return a flattened version of a given 2-D matrix (list-of-lists)'''
    return [item for row in matrix for item in row]


def negative_matrix(matrix):
    return [[-n for n in row] for row in matrix]


def zip_matrix(matrix):
    return list(zip(*matrix))  # == [col for col in zip(*matrix)]


def words_processing(filename):
    with open(filename) as file:
        # trip the righttrailing of all words
        words = (line.rstrip() for line in file)  # generator expression
        # store all long words
        words_over_five_letters = (word for word in words if len(word) > 5)
        # store the reverse of all long words
        reversed_words = (word[::-1] for word in words_over_five_letters)
        # store all reversible words
        reversible_words = (word for word in words_over_five_letters if word in reversed_words)

        # print all words which are reversible
        print(*reversible_words)


data = [('blue', 0.2), ('red', 0.3), ('green', 0.5)]
flipped_data = ((frequency, color) for color, frequency in data)

with open('data.csv', mode='wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(flipped_data)


def find_unique_letters(text):  # Using a comprehension and a Counter object to find a set of unique letters in a given string
    return {char for char, count in Counter(text.lower()).items() if count == 1}


def interleave(*args):
    return (item for row in zip(*args) for item in row)


def interleave_longest(*args):
    return (item for row in zip_longest(*args) for item in row)


print(list(interleave([1, 2, 3, 4], [5, 6, 7, 8], [2, 3, 4], [7, 8, 9])))
print(list(interleave_longest([1, 2, 3, 4], [5, 6, 7, 8], [2, 3, 4], [7, 8, 9])))
