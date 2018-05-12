test_list = [3, 8, 12, 15, 20, 28, 25, 16, 11]
def searchrecursive(A, head, tail):
    if(head == tail):
        return A[head]
    else:
        mid = int((head+tail) / 2)
        if(A[mid] < A[mid+1]):
            result = searchrecursive(A, mid+1, tail)
        if(A[mid] > A[mid+1]):
            result = searchrecursive(A, head, mid)
        return result
print(searchrecursive(test_list, 0, len(test_list) - 1))
