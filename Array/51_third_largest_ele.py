from get_array_helper import take_array_user
from math import inf
def get_third_max(arr , n):
    if n<3:
        return "not Possible"
    MAX1 = MAX2 = MAX3 = inf * -1
    for i in arr:
        if i>MAX1:
            MAX3 = MAX2
            MAX2 = MAX1
            MAX1 = i
        elif i>MAX2:
            MAX3 = MAX2
            MAX2 = i
        elif i>MAX3:
            MAX3 = i
    return MAX3

arr , n = take_array_user()
print("Third largest element in the array is : ",get_third_max(arr , n))