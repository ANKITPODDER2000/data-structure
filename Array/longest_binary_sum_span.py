def longest_span_sum(arr1 , arr2 , n):
    maxlen = 0
    stack  = [-1] * (2*n+1)
    presum1 = presum2 = 0
    for i in range(n):
        presum1 += arr1[i]
        presum2 += arr2[i]
        diff = presum1 - presum2
        diffindex = n + diff
        if diff==0:
            maxlen = i+1
        elif stack[diffindex] == -1:
            stack[diffindex] = i
        else:
            length = i - stack[diffindex]
            if length > maxlen:
                maxlen = length
    return maxlen

print("Enter the array1 : ",end="")
arr1 = [int(x) for x in input().split(" ")]
print("Enter the array2 : ",end="")
arr2 = [int(x) for x in input().split(" ")]
n = len(arr1)
print(longest_span_sum(arr1 , arr2 , n))