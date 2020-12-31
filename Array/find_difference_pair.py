from get_array_helper import take_array_user
def get_pairs(arr , n , diff):
    HASH = {}
    for i in range(n):
        num1 = diff+arr[i]
        num2 = (diff-arr[i]) * -1
        if num1 in HASH or num2 in HASH:
            return True
        HASH[arr[i]] = True
    return False
arr , n = take_array_user()
diff = 6
print("isPresent 6 diff : ",get_pairs(arr , n , diff))