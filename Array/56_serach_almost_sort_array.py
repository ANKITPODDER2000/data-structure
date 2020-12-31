from get_array_helper import take_array_user
def search(arr , s , e,key):
    if s<=e:
        mid = (s+e) // 2
        if arr[mid]==key:
            return mid
        elif (mid > 0 and arr[mid-1]==key):
            return mid -1
        elif (mid <= e-1 and arr[mid+1]==key):
            return mid+1
        elif arr[mid]>key:
            search(arr , s , mid-1 ,key)
        else:
            search(arr , mid+1 , e , key)
    return -1

arr , n = take_array_user()
print("Pos : ",search(arr , 0 , n-1 , int(input("Enter the key : "))))