#Follow up for Remove Duplicates, what if duplicates are allowed at most twice?
#For example, Given sorted array A = [1,1,1,2,2,3]
#Your function should return length = 5 and A is now [1,1,2,2,3]
def solution(A):
    if len(A) == 0:
        return 0
    else:
        j = 0
        num = 0 #用一个计数器记录它重复的次数
        for i in range(1, len(A)):
            if(A[j] == A[i]): #如果重复次数小于等于2，按前一个题目的方式处理
                num += 1
                if num < 2:
                    j += 1
                    A[j] = A[i]
            else:            #否则继续按前一个题目的方式处理，并清空计数器的值
                j += 1
                A[j] = A[i]
                num = 0




                
test = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
solution(test)
print(test)
