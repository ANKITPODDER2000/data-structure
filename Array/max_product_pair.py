import math
from get_array_helper import take_array_user
def find_max_product(arr , n):
    max1 = max2 = math.inf * -1
    n_neg = 0
    for i in range(n):
        if arr[i]>max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i]>max2:
            max2 = arr[i]
        if arr[i]<0:
            n_neg += 1
    if n_neg<=1:
        return max2*max1
    min1 = min2 = math.inf
    for i in range(n):
        if arr[i]<min1:
            min2 = min1
            min1 = arr[i]
        elif min2>arr[i]:
            min2 = arr[i]
    if min1*min2 > max1*max2:
        return min1*min2
    return max1*max2
arr , n = take_array_user()
print("Max product is : ",find_max_product(arr , n))