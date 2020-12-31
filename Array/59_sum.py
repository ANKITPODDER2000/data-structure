from get_array_helper import take_array_user
def sum_(arr , n):
    s = 0
    for i in range(n):
        s = s + arr[i]
    return s

arr , n = take_array_user()
print("Sum of this array is : ",sum_(arr , n))