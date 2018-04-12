import random
import time

def insert_sort(A,n):
    j = 0
    for i in range(0,n-1):
        j = i
        key = A[j+1]
        #print("key =",key)
        while((key < A[j]) & (j >= 0)):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
            
test = [random.randint(1,800000) for i in range(10000)]

#print(test)

start = time.time()
insert_sort(test, len(test))
print("Time used:", time.time()-start)

#print(test)
