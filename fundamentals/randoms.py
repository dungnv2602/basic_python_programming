import random

value = random.randint(1, 10)
print(value)

greetings = ['Hello', 'HI', 'Hey', 'Howdy', 'Hola']

value = random.choice(greetings)
print(value)

colors = ['Red', 'Black', "green"]
value = random.choices(colors, k=10)
print(value)

deck = list(range(1, 53))
print(deck)

random.shuffle(deck)
print(deck)

hand = random.sample(colors, k=5)

