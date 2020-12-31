from get_array_helper import take_array_user
import math
def get_max_pair(arr , n):
    MAX1 = math.inf * -1
    MAX2 = MAX1
    for i in range(n):
        if arr[i]>MAX1:
            MAX2 = MAX1
            MAX1 = arr[i]
        elif arr[i]>MAX2:
            MAX2 = arr[i]
    return MAX1+MAX2
arr , n = take_array_user()
print("MAX PAIR SUM : ",get_max_pair(arr , n))