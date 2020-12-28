def leaders(arr , n):
    MIN = arr[-1]
    print("Leaders are : ",end="")
    print(arr[-1],end=" ")
    for i in range(n-1 , -1 , -1):
        if arr[i]>MIN:
            MIN = arr[i]
            print(MIN , end=" ")
print("Enter the array : ",end="")
arr = [int(x) for x in input().split(" ")]
n   = len(arr)
leaders(arr , n)