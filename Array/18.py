def frequencycount(A,N):
    li = [0] * N
    for i in A:
        li[i-1] += 1
    A = li[:]