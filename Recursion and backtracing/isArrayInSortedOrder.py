def is_array_sorted(A):
    if len(A) == 1:
        return True
    return (A[0] <= A[1] and is_array_sorted(A[1:]))

A = [1,2,3,4,5,6,7,8]
print(is_array_sorted(A))
B = [2,1,3,4,1,5,6]
print(is_array_sorted(B))
C = [4,3,2,1]
print(is_array_sorted(C))