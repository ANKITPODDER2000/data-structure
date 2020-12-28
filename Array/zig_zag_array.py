from typing import final
from get_array_helper import take_array_user
def print_zig_zag(arr , n):
    zig = True
    for i in range(n-1):
        if zig:
            if arr[i]>arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
        zig = not zig
arr , n = take_array_user()
print_zig_zag(arr , n)
print(arr)