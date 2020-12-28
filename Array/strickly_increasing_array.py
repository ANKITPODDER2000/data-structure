from get_array_helper import take_array_user
def get_increasing_arrays(arr , n):
    count = 1
    ans = 0
    for i in range(1 , n):
        if arr[i-1] < arr[i]:
            count += 1
        else:
            ans += (count * (count - 1)) // 2
            count = 1
    try:
        if arr[-2]<arr[-1]:
            ans += (count * (count - 1)) // 2
            count = 1
    except:
        pass
    return ans
arr , n = take_array_user()
ans = get_increasing_arrays(arr , n)
print("No of increasing sub array : ",ans)