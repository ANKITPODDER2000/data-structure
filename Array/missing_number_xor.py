def missing_value(arr1 , n):
    s = 1
    for i in range(2 , n+2):
        s = s ^ i
    for i in arr1:
        s = s ^ i
    return s

print("Enter the array : ",end="")
arr = [int(x) for x in input().split()]
n   = len(arr)
print(missing_value(arr , n))