from get_array_helper import take_array_user

def move_zeros(arr , n):
    i=j=0
    while i<n:
        if arr[i]!=0:
            arr[j] , arr[i] = arr[i] , arr[j]
            j+=1
        i+=1

arr ,n = take_array_user()
move_zeros(arr , n)
print("Modified arr is : ",arr)