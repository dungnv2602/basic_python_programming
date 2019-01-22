from datetime import datetime
first_name = 'Dung'
last_name = "Nguyen"

sentence = "My nameis {} {}".format(first_name, last_name)

sentence = f"My name is {first_name.upper()} {last_name}"

person = {'name': 'Jenn', 'age': 23}

sentence = f"my name is {person['name']} {person['age']}"

for n in range(1, 11):
    sentence = f"The value is {n:02}"
    print(sentence)

pi = 3.12341231

print(f"Pi number: {pi:.2f}")


birthday = datetime(1990, 1, 1)
print(f"{birthday:%B%d,%Y}")
