from get_array_helper import take_array_user
def MAXCOUNT(arr , n):
    MAX_LEN = 1
    for i in range(n-1):
        MIN = MAX = arr[i]
        for j in range(i+1,n):
            MIN = min(MIN , arr[j])
            MAX = max(MAX , arr[j])
            if MAX-MIN == j-i:
                MAX_LEN = max(MAX_LEN , j-i+1)
    return MAX_LEN
arr , n = take_array_user()
print(MAXCOUNT(arr , n))