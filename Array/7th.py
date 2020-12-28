class Solution:
    def countZeroes(self, arr, n):
        if n <=2:
            return arr.count(0)
        l = 0
        r = n-1
        
        while True:
            mid = (r + l) // 2
            #print(l,r , mid)
            if arr[0]==0:
                return n
            elif arr[n-1]==1:
                return 0
            elif arr[mid]==1 and arr[mid+1]==0:
                return n-mid-1
            elif arr[mid]==0 and arr[mid-1]==1:
                return n-mid
            elif arr[mid]==0:
                r = mid-1
            else:
                l = mid+1
        
                
s = Solution()
a = [1,0,0,0,0,0]
A = s.countZeroes(a, len(a))
print(A)