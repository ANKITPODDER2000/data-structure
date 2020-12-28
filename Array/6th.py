#User function Template for python3
class Solution:

    def findMaximum(self,arr, n):
        if n<=2:
            return max(arr)
        l = 0
        r = n-1
        count = 0
        while l<=r:
            mid = (l + r) // 2
            #print(l,r , mid)
            if mid==0:
                if arr[mid] > arr[mid+1]:
                    return arr[mid]
            elif mid == n-1:
                return arr[mid]
            elif arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return arr[mid]
            try:
                if arr[mid] > arr[mid+1]:
                    #print("HEY" , arr[mid] , arr[mid+1])
                    r = mid-1
                else:
                    l = mid+1
            except:
                return arr[mid]
            count += 1
            if count > 6:
                break
                
            
s = Solution()
li = [1 , 2 , 3 , 2 , 1 ]
a = s.findMaximum(li, len(li))
print(a)