# 1 2 3 4 5 6
# 6 1 2 3 4 5
# We just have to swap the last element and first element 
from get_array_helper import take_array_user
def rotateByOne(arr , n):
    ele_last = arr[n-1]
    for i in range(n-1 , 0 , -1):
        arr[i] = arr[i-1]
    arr[0] = ele_last
arr , n = take_array_user()
rotateByOne(arr ,n)
print("Array after rotating : ",arr)