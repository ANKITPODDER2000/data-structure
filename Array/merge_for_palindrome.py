from get_array_helper import take_array_user
def merge_palindrome(arr , s , e):
    if s==e:
        return 0
    else:
        if arr[s]==arr[e]:
            return merge_palindrome(arr , s+1 , e-1)
        elif arr[s]>arr[e]:
            arr[e-1] = arr[e-1] + arr[e]
            return 1 + merge_palindrome(arr , s , e-1)
        else:
            arr[s+1] = arr[s+1] + arr[s]
            return 1 + merge_palindrome(arr , s+1 , e)

arr , n = take_array_user()
ans = merge_palindrome(arr , 0 , n-1)
print("ANS IS : ",ans)