import random
import time

def Merge(A, p, q, r):
    Left = A[p:q+1]
    Right = A[q+1:r+1]
    Left.append(float('inf'))
    Right.append(float('inf'))
    i = 0
    j = 0
    for x in range(p, r+1):
        if(Left[i] < Right[j]):
            A[x] = Left[i]
            i += 1
        else:
            A[x] = Right[j]
            j += 1
def Merge_sort(A,p,q):
    if(p<q):
        mid = int( (p+q)/2 )
        Merge_sort(A, p, mid)
        Merge_sort(A, mid+1,q)
        Merge(A,p,mid,q)

test = [random.randint(0,800000) for i in range(1000)]
start = time.time()
Merge_sort(test,0,len(test)-1)
if(test == sorted(test)):
    print("OK!")
else:
    print("Error!")
print("Time Used:",time.time() - start)
