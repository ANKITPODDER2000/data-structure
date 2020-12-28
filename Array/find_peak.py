from get_array_helper import take_array_user
def binary_search(arr , s ,e):
    mid = (s+e) // 2
    if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
        return mid
    elif mid>0 and (arr[mid-1]>arr[mid]):
        return binary_search(arr , s , mid-1)
    else:
        return binary_search(arr , mid+1 , e)
def peak(arr , n):
    return binary_search(arr , 0 ,n-1)
arr , n = take_array_user()
p = peak(arr , n)
print("Fixed point in the given array is : ",arr[p])