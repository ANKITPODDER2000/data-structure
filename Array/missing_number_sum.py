def missing_value(arr1 , n):
    sum1 = (n+1)*(n+2) // 2
    sum2 = sum(arr1)
    return sum1 - sum2

print("Enter the array : ",end="")
arr = [int(x) for x in input().split()]
n   = len(arr)
print(missing_value(arr , n))