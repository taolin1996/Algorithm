#Remove Element
#Given an array and a value, remove all instance of that > value in place and return the new length
#The order of elements can be changed. It doesn't matter what you leave beyond the new length
import random

def solution(A, value):
    return [i for i in A if i > value]

test = [i for i in range(100)]
result = solution(test,50)
random.shuffle(result)
print(result)
print(len(result))

