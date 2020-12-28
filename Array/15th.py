def missingNumber(arr,n):
    A = [0] * (n+2)
    for i in arr:
        if i>0 and i<(n+2):
            A[i] += 1
    for i in range(1 , n+2):
        if A[i] == 0:
            return i
        
arr = [10,50,60,20,10]
n = len(arr)
print(missingNumber(arr, n))