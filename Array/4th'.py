def findTriplets(arr,n):
    arr = sorted(arr)
    b = 0
    for i in range(0 , n -2):
        l = i+1
        r = n-1
        while l < r:
            if arr[i] + arr[l] + arr[r] == 0:
                return 1
            elif arr[i] + arr[l] + arr[r] > 0:
                r -= 1
            else:
                l += 1
    return b
    

li = [int(x) for x in input().split(' ')]
#################################

print(findTriplets(li, len(li) ))

#-3 -1 0 1 2