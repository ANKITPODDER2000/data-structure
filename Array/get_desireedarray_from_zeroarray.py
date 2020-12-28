from get_array_helper import take_array_user
def get_min_two_pow(MIN):
    if MIN<=1:
        return 0 , 0
    i = 1
    count = 0
    while i*2 <= MIN:
        i = i * 2
        count += 1
    return (i , count)

def noOfOperation(arr , n):
    MIN = min(arr)
    min_two_pow , p  = get_min_two_pow(MIN)
    ans = 0
    if min_two_pow > 0:
        ans = n + p
    for i in range(n):
        ans += (arr[i] - min_two_pow)
    return ans

arr , n = take_array_user()
print("No of operations : ",noOfOperation(arr , n))