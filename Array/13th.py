def maxSumPath(ar1, ar2, m, n):
    i, j = 0, 0
    result, sum1, sum2 = 0, 0, 0
    while (i < m and j < n):
        if ar1[i] < ar2[j]:
            sum1 += ar1[i]
            i += 1
        elif ar1[i] > ar2[j]:
            sum2 += ar2[j]
            j += 1
 
        else:
            result += max(sum1, sum2)
            sum1, sum2 = 0, 0
            temp = i
            while i < m and ar1[i] == ar2[j]:
                sum1 += ar1[i];
                i += 1
            while j<n and ar1[temp] == ar2[j]:
                sum2 += ar2[j]
                j += 1
            result += max(sum1,sum2)
            sum1 = sum2 = 0;           
    while i < m:
        sum1 += ar1[i]
        i += 1
    while j < n:
        sum2 += ar2[j]
        j += 1
    result += max(sum1, sum2)
 
    return result

arr1 = [1,2,3]
m = len(arr1)
arr2 = [3,4,5]
n = len(arr2)
ans = maxSumPath(arr1, arr2, m, n)
print(ans)