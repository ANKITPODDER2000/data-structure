# 1 2 3 4 5 6
# 3 4 5 6 1 2
#No efficient way
from get_array_helper import take_array_user
def rotate_arr(arr , n , rotate_deg = 1):
    rotate_deg %= n
    l_arr = arr[:rotate_deg]
    r_arr = arr[rotate_deg : ]
    count = 0
    for i in r_arr:
        arr[count] = i
        count += 1
    for i in l_arr:
        arr[count] = i
        count += 1
arr , n = take_array_user()
rotate_arr(arr , n , int(input("Enter the rotate degree : ")))
print("Array after rotating : ",arr)