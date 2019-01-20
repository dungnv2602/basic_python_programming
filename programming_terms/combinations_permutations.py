# •	Combinations & Permutations:
# o	Permutations are for lists (order matters) and
# o	combinations are for groups (order doesn’t matter).
import itertools
word = 'sample'
my_letters = 'plmeas'

combinations = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)

for p in permutations:
    # print p
    if ''.join(p) == word:
        print('Match!')
        break
else:
    print('No Match!')
