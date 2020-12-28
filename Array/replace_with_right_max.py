from get_array_helper import take_array_user
def modify_array(arr , n):
    MAX = arr[-1]
    temp = MAX
    for i in range(n-1 , -1 , -1):
        if arr[i]>MAX:
            temp = arr[i]
        arr[i] = MAX
        MAX = temp
    arr[-1] = -1
arr , n = take_array_user()
modify_array(arr , n)
print("Modified array is : ",end="")
for i in arr:
    print(i , end=" ")