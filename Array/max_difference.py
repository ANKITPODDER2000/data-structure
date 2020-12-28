from math import inf
from get_array_helper import take_array_user
def max_dif(arr , n):
    MAX = inf * -1
    min = arr[0]
    for i in range(1 , n):
        if arr[i]-min > MAX:
            MAX = arr[i]-min 
        if arr[i] < min :
            min = arr[i]
    return MAX

arr , n = take_array_user()
print(max_dif(arr , n))