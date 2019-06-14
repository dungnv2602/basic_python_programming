book_title = ['great','expectations','the','adventures','of',
'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {} # empty dictionary

for word in book_title:
    if word not in word_counter:    
        word_counter[word] = 1
    else:
        word_counter[word] += 1   

for word in book_title:
    word_counter[word] = word_counter.get(word,0)+1

print(word_counter)

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }


for key in cast:
    print(key)

for key, value in cast.items():
    print('Actor: {}; Role: {}'.format(key,value))
