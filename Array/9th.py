import math
#User function template for Python

class Solution:	
    def remove_duplicate(self, A, N):
        cur_val = -math.inf
        l = 0
        for i in range(N):
            if A[i] != cur_val:
                A[l] = A[i]
                l += 1
                cur_val = A[i]
        return A[:l]
    
s = Solution()
A = []
N = len(A)
ans = s.remove_duplicate(A, N)
print(ans)
                