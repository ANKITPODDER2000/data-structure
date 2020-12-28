import sys
from get_array_helper import take_array_user
def min_difference(arr , n):
    arr.sort()
    MIN = sys.maxsize
    for i in range(n-1):
        if MIN > arr[i+1] - arr[i]:
            MIN = arr[i+1] - arr[i]
    return MIN

arr , n = take_array_user()
min_diff = min_difference(arr , n)
print("Min diff is : ",min_diff)