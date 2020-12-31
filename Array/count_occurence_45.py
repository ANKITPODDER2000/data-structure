from get_array_helper import take_array_user
def binary_serach(arr , s , e , key):
    if s<=e:
        mid = (s+e) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid]>key:
            return binary_serach(arr , s , mid-1 , key)
        else:
            return binary_serach(arr , mid+1 , e , key)
    return -1
def count_occur(arr ,n ,key):
    pos = binary_serach(arr , 0 , n-1 , key)
    count = 0
    if pos==-1:
        print("Not Possible!")
        return
    temp_pos = pos
    while temp_pos>=0 and arr[temp_pos]==key:
        count += 1
        temp_pos -= 1
    temp_pos = pos+1
    while temp_pos < n and arr[temp_pos]==key:
        count += 1
        temp_pos += 1
    print("Count of %d is : %d"%(key , count))

arr ,n = take_array_user()
count_occur(arr , n , int(input("Enter the key : ")))