import random
import time

#pop()方法占用的时间过大，导致所用时间比用哨兵的时间多得多
def Merge(A, p, q, r):
    Left = A[p:q+1]
    Right = A[q+1:r+1]
    i = 0
    j = 0
    for x in range(p, r+1):
        #print("Left =", Left)
        #print("Right =", Right)
        if(len(Left) == 0):
            A[x:x+len(Right)] = Right[:]
            return
        elif(len(Right) == 0):
            A[x:x+len(Left)] = Left[:]
            return
        elif(Left[0] < Right[0]):
            A[x] = Left.pop(0)
            i += 1
        else:
            A[x] = Right.pop(0)
            j += 1
def Merge_sort(A,p,q):
    if(p<q):
        mid = int( (p+q)/2 )
        Merge_sort(A, p, mid)
        Merge_sort(A, mid+1,q)
        Merge(A,p,mid,q)

test = [random.randint(0,800000) for i in range(100000)]
#test = [2,4,8,1,3,5]
start = time.time()
#Merge(test,0,2,5)
Merge_sort(test,0,len(test)-1)
#print(test)

if(test == sorted(test)):
    print("OK!")
else:
    print("Error!")
print("Time Used:",time.time() - start)
