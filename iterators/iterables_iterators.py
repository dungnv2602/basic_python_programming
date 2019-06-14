'''
Iterable:
    •	Is an object that can return one of their elements at a time such as a list.
    •	has dunder method __iter()__  can be looped over
    •	What the for loop doing in the background is calling the __iter()__ on iterable object and returning an iterator that we can loop over

Iterator:
    •	Is an object that represents a stream of data with a state so that it remembers where it is during iteration
    •	Get the next value using __next__  list doesn’t have __next__  list is not an iterator
    •	Has __iter__  return itself
    •	Only go forward using __next__
    •	Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.
'''
nums = [1, 2, 3]

iterator_nums = iter(nums)

print(next(iterator_nums))  # remember the state
print(next(iterator_nums))  # remember the state
print(next(iterator_nums))  # remember the state

for num in nums:
    print(num)

# Custom Iterator (also a iterable)


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)
for num in nums:
    print(num)

# custom iterator Sentence


class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)

# generator


def sentence(sentence):
    for word in sentence.split():
        yield word


for word in sentence('My generator'):
    print(word)
