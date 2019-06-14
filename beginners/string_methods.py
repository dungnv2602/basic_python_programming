verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
length = len(verse)
first_occurance = verse.find('and')
last_occurance = verse.rfind('you')
numbers = verse.count('you')
print("Length: {}; First Index Of \'and': {}; Last Index Of \'you': {}; Count Of \'you': {}"
.format(length, first_occurance, last_occurance, numbers))