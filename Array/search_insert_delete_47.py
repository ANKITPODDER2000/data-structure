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
def insert(arr , n ,pos):
    if pos>=n:
        print("Not Possible !!!")
    for i in range(n-1 , pos-1 , -1):
        arr[i+1] = arr[i]
    arr[pos] = int(input("Enter the element to insert in pos %d : "%pos))
def delete(arr , n , ele):
    pos = binary_serach(arr , 0 , n-1 , ele)
    if pos == -1:
        print("Not found!")
        return
    for i in range(pos , n-1):
        arr[i] = arr[i+1]
    return arr[:-1]
