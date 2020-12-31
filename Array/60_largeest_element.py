from get_array_helper import take_array_user
def max_(arr , n):
    MAX = arr[0]
    for i in range(1,n):
        if arr[i]>MAX:
            MAX = arr[i]
    return MAX

arr , n = take_array_user()
print("Max value in this array is : ",max_(arr , n))