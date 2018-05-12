#Remove Duplicates from Sorted Array
#Given a sorted array, remove the duplicates in place such that > each element appear only once and return the new length
#Do not allocate extra space for anther array, you must do this in place with constant memory
#For example, Given input array A = [1,1,2]
#Your function should return length = 2, and A is now [1,2]
import random

def solution(A):
    if(len(A) == 0):
        return 0
    j = 0
    for i in range(len(A)):
        if(A[j] != A[i]):
            j += 1
            A[j] = A[i]
    return A[:j+1]
            

test = [1,1,1,1,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4]

print(solution(test))

