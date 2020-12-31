from get_array_helper import take_array_user
from math import inf
def get_min(arr , n):
    min1 = min2 = inf
    for i in range(n):
        if arr[i]<min1:
            min2 = min2
            min1 = arr[i]
        elif arr[i]<min2 and arr[i]!=min1:
            min2 = arr[i]
    if min1!=inf and min2!=inf:
        print("MIN1 : %d\nMIN2 : %d\n"%(min1,min2))
    elif min2==inf:
        print("MIN1 : %d\nMIN2 : None\n"%(min1))

arr , n = take_array_user()
get_min(arr , n)