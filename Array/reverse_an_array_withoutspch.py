def reverse_array(arr , n):
    i = 0
    j = n-1
    # print()
    # print(i,j)
    while i<j:
        if ((arr[i]>='a' and arr[i]<='z') or (arr[i]>='A' and arr[i]<='Z')) and (arr[j]>='a' and arr[j]<='z') or (arr[j]>='A' and arr[j]<='Z'):
            arr[i] , arr[j] = arr[j] , arr[i]
            i+=1
            j -= 1
        elif (arr[i]>='a' and arr[i]<='z') or (arr[i]>='A' and arr[i]<='Z'):
            j-=1
        else:
            i+=1
print("Enter the char array : ",end="")
arr = [a for a in input().split(" ")]
n = len(arr)
print("Array is   : ",end="")
for i in arr:
    print(i , end="")
reverse_array(arr , n)
print("\nMod arr is : ",end="")
for i in arr:
    print(i , end="")