from get_array_helper import take_array_user
def segregrate(arr , n):
    i = 0
    j = 0
    while j < n:
        if arr[j] == 0:
            arr[i],arr[j] = arr[j] , arr[i]
            i += 1
        j += 1
arr ,n = take_array_user()
segregrate(arr , n)
print("Array is : ",end="")
for i in arr:
    print(i , end=" ")