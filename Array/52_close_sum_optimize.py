from get_array_helper import take_array_user
from math import inf
def closest_sum(arr , n , num):
    ans = None
    diff = inf
    arr.sort()
    l = 0
    r = n-1
    while l<r:
        if abs(arr[l]+arr[r]-num)<diff:
            diff = abs(arr[l]+arr[r]-num)
            ans = arr[l]+arr[r]
        if arr[l]+arr[r] > num:
            r -= 1
        else:
            l += 1
    return ans

arr , n = take_array_user()
print("Closest pair sum is : %d"%(closest_sum(arr , n , int(input("Enter the num : ")))))
