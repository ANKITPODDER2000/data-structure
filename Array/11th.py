#User function Template for python3
def mergeArrays(a,b,n,m):
    arr = [0] * (n+m)
    l = 0
    r = 0
    count = -1
    while l<n or r<m:
        if l==n:
            if arr[count] != b[r]:
                count += 1
                arr[count] = b[r]
            else:
                r+=1
        elif r==m:
            if arr[count] != a[l]:
                count += 1
                arr[count] = a[l]
            else:
                l+=1
        else:
            if a[l] < b[r]:
                count += 1
                arr[count] = a[l]
            else:
                count += 1
                arr[count] = b[r]
            while l<n and arr[count]==a[l]:
                l+=1
            while r<m and arr[count]==b[r]:
                r+=1
    return arr[:count+1]

a = [1,1,1,1,1,1,1]
b = [1,1,1,1,1]
n = len(a)
m = len(b)
arr = mergeArrays(a, b, n, m)
print(arr)