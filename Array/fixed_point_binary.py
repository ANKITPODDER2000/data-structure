from get_array_helper import take_array_user
def binary_search(arr , s ,e):
    if s<=e:
        mid = (s+e) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid]>mid:
            return binary_search(arr , s , mid-1)
        else:
            return binary_search(arr , mid+1 , e)
    else:
        return -1
def find_fixpoint(arr , n):
    return binary_search(arr , 0 ,n-1)
arr , n = take_array_user()
fixpoint = find_fixpoint(arr , n)
print("Fixed point in the given array is : ",fixpoint)