from functools import reduce

numbers = [4,5]

sum = reduce(lambda x,y: x+y, numbers)

print(sum)