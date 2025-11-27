import random

def rand(x,y):
    while True:
            yield random.randint(x,y)

infinite_generator = rand(1, 100)

for number in infinite_generator:
    print(number)
    user_input = input()
    if user_input.lower() == "b":
         break