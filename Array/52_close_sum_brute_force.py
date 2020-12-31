from get_array_helper import take_array_user
from math import inf
def closest_sum(arr , n , num):
    ans = None
    diff = inf
    for i in range(n):
        for j in range(i , n-1):
            if abs(arr[i]+arr[j] - num) < diff:
                diff = abs(arr[i]+arr[j] - num)
                ans = arr[i]+arr[j]
    return ans
arr , n = take_array_user()
print("Closest pair sum is : %d"%(closest_sum(arr , n , int(input("Enter the num : ")))))
