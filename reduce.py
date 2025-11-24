from functools import reduce

numbers = [4,5,10,2,6,20]

sum = reduce(lambda x,y: x+y, numbers)

print(sum)