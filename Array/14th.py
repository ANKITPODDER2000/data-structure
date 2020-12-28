def bin_search(arr , n, x):
    l = 0
    h = n - 1
    while(l <= h): 
        mid = int((l + h) / 2)
        if(arr[mid] <= x): 
            l = mid + 1; 
        else:
            h = mid - 1
    return h 
            
def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    arr2.sort()
    ans = [0] * n1
    for i in range(n1):
        ans[i] = bin_search(arr2, n1, arr1[i]) + 1
    return ans
        
arr1 = [int(x) for x in input().split()]
n1   = len(arr1)
arr2 = [int(x) for x in input().split()]
n2   = len(arr2)
print(countEleLessThanOrEqual(arr1, n1, arr2, n2))