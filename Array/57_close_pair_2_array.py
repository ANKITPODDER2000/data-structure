from get_array_helper import take_array_user
from math import inf
def close_pair(arr1 , n1 , arr2 ,n2 , num):
    l = 0
    r = n2-1
    diff = inf
    ans = None
    while l<n1 and r>=0:
        if abs(arr1[l]+arr2[r]-num)<diff:
            diff = abs(arr1[l]+arr2[r]-num)
            ans  = arr1[l]+arr2[r]
        if arr1[l]+arr2[r] > num :
            r -= 1
        else:
            l += 1
    return ans
arr1 , n1 = take_array_user()
arr2 , n2 = take_array_user()
print("Close pair : ",close_pair(arr1,n1,arr2,n2,int(input("Enter the num : "))))