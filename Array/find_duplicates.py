from get_array_helper import take_array_user
def find_duplicates(arr , n):
    print("Duplicates are : ",end="")
    for i in range(n):
        temp = arr[abs(arr[i])]
        if temp==None:
            continue
        elif temp>0:
            arr[abs(arr[i])] = arr[abs(arr[i])] * -1
        else:
            print(abs(arr[i]) , end=" ")
            arr[abs(arr[i])] = None
arr , n = take_array_user()
find_duplicates(arr , n)