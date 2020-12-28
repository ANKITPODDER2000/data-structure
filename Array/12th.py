def equilibriumPoint(A, N):
    if N==1:
        return 1
    s = sum(A)
    ls = 0
    for i in range(N):
        if s-ls-A[i] == ls:
            return i+1
        ls += A[i]
    return -1
A = [1,3,5,2,2]
N = len(A)
ans = equilibriumPoint(A, N)
print(ans)