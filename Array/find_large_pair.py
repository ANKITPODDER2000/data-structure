from get_array_helper import take_array_user
def find_arr_pair(arr ,n):
    max1 = max(arr[0] , arr[1])
    max2 = min(arr[0] , arr[1])
    for i in range(2 , n):
        if arr[i]>max1:
            max2 = max1
            max1 = arr[i]
        elif max2>arr[i]:
            arr[i] = max2
    return max1+max2
arr , n = take_array_user()
print("MAX PAIR SUM is %d"%find_arr_pair(arr,n))