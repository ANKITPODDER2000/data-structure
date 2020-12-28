from get_array_helper import take_array_user
def max_len(arr , n):
    inc = [1] * n
    dec = [1] * n
    for i in range(1 , n):
        if arr[i]>arr[i-1]:
            inc[i] = inc[i] + inc[i-1]
        else:
            inc[i] = inc[i-1]
    for i in range(n-2 , -1 , -1):
        if arr[i]>arr[i+1]:
            dec[i] = dec[i] + dec[i+1]
        else:
            dec[i] = dec[i+1]
    MAX_LEN = inc[0] + dec[0] -1
    for i in range(1,n):
        if (inc[i] + dec[i] - 1) >MAX_LEN:
            MAX_LEN = inc[i] + dec[i] - 1
    return MAX_LEN


arr , n = take_array_user()
print("MAX LENGTH OF BITCOIN SERIES IS : ",max_len(arr , n))