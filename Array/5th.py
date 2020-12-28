def convertToWave(A,N):
    count = 0
    for i in range(0 , N//2 ):
        A[count] , A[count+1] = A[count+1] , A[count]
        count += 2
    return A

A = [2,4,7,8,9,10]
ans = convertToWave(A , len(A))
print(ans)