# 1 2 3 4 5 6
# 3 4 5 6 1 2
#No efficient way
from get_array_helper import take_array_user
def reverse_(arr , s , e):
    ele = (e-s+1) // 2
    for i in range(ele):
        arr[s+i] , arr[e-i] = arr[e-i] , arr[s+i]

def rotate_arr(arr , n , rotate_deg = 1):
    rotate_deg %= n
    reverse_(arr, 0 , rotate_deg-1)
    reverse_(arr , rotate_deg , n-1)
    reverse_(arr , 0 , n-1)
arr , n = take_array_user()
rotate_arr(arr , n , int(input("Enter the rotate degree : ")))
print("Array after rotating : ",arr)