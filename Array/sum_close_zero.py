from get_array_helper import take_array_user
def get_min_sum(arr , n):
    arr.sort()
    SUM = abs(arr[0] + arr[-1])
    l = 1
    r = n-2
    while l < r:
        s = arr[l] + arr[r]
        if SUM > abs(s):
            SUM = abs(s)
        if s<0:
            l+=1
        else:
            r-=1
    return SUM
arr , n = take_array_user()
print("MIN SUM CLOSE TO ZERO IS : ",get_min_sum(arr , n))