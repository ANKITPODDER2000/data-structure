class Solution:
    def celebrity(self, M, n):
        outdegree = [0] * n
        indegree = [0] * n
        for i in range(n):
            for j in range(n):
                indegree[j] += M[i][j]
                outdegree[i] += M[i][j]
        for i in range(n):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i
        return -1
                
    
    
M = [
     [0,1,0],
     [0,0,1],
     [0,1,0]
]
s = Solution()
ans = s.celebrity(M , len(M))
print(ans)