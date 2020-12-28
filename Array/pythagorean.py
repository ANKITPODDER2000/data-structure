from get_array_helper import take_array_user
def pythagorean(arr , n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]
    arr.sort()
    i = n-1
    while i>=2:
        j = 0
        k = i-1
        while j<k:
            if arr[j]+arr[k] == arr[i]:
                # print("Triangle sides are : ",arr[j],arr[k],arr[i])
                return True
            elif arr[j]+arr[k] > arr[i]:
                k -= 1
            else:
                j += 1
        i -= 1
    return False
arr , n = take_array_user()
print("There is pythagorean triplate : ",pythagorean(arr ,n))