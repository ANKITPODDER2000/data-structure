from get_array_helper import take_array_user
def number_occuring_odd(arr , n):
    number = arr[0]
    for i in range(1 , n):
        number ^= arr[i]
    return number
arr , n = take_array_user("Enter the array")
ans = number_occuring_odd(arr , n)
print("Number which is occuring odd no of times : ",ans)