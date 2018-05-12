#coding=utf-8  
import random
Total_num = 0
#风格1  
def queen(A, cur=0):
    global Total_num
##    print("Enter queen(A =",A,"cur =",cur,")")
    if cur==8:
        Total_num += 1
##        output(A)  
    else:  
        for col in range(8):  
            A[cur] = col #表示把第cur行的皇后放在col列上   
            if check(A,col,cur):  
                queen(A, cur+1)
##    print("Exit queen(A =",A,"cur =",cur,")")
    
def check(A,col,cur):
    for r in range(cur):  
        if A[r]==col or r-A[r]==cur-A[cur] or r+A[r]==cur+A[cur]:#判断是否跟前面的皇后冲突
            return False
    return True
def output(A):
    for row in range(8):
        for col in range(8):
            if(row == A[col]):
                print("Q",end = " ")
            else:
                print(".", end = " ")
        print()
queen([None]*8)  
print("总数为",Total_num,"个")
