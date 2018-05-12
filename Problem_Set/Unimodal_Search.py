test_list = [1,4,6,11,22,25,20,19,17,13]
def searchmaxim(A, n):
    a, b = 0, n
    while(a < b):
        mid = int((a+b) / 2)
        if(A[mid] < A[mid + 1]):
            a = mid + 1
        if(A[mid] > A[mid + 1]):
            b = mid
    return A[a]

print(searchmaxim(test_list, len(test_list)-1))


