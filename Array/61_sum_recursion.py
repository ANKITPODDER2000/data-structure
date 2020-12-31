from get_array_helper import take_array_user

def rec_sum(arr , pos , n):
    if pos==n:
        return 0
    return arr[pos] + rec_sum(arr , pos+1 , n)

def sum_(arr , n):
    return rec_sum(arr , 0 , n)

arr , n = take_array_user()
print("Sum of this array is : ",sum_(arr , n))