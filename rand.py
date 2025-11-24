import random

def rand(x,y,z):
    for i in range(z):
        yield random.randint(x,y)

list = []
for number in rand(1,50,10):
    list.append(number)

print(list)