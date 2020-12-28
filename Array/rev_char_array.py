def reverse(arr , n ):
    for i in range(n//2):
        arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
print("Enter the car array : ",end="")
arr = [x for x in input().split()]
reverse(arr , len(arr))
print(arr)