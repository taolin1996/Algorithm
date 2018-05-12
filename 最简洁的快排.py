import random
def sort(ls):
    return [] if ls == [] else sort([y for y in ls[1:] if y < ls[0]]) + [ls[0]] + sort([y for y in ls[1:] if y >= ls[0]])
    
test = [i for i in range(100)]

random.shuffle(test)
print(test)
print(sort(test))

