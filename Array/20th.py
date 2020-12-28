def maxSubArraySum(a,size):
    ans = a[0]
    s   = a[0]
    for i in range(1,size):
        if s<0:
            s = 0
        s += a[i]
        #print(s , ans)
        if s>ans:
            ans = s
    return ans

a = [int(x) for x in input().split()]
size = len(a)
print(maxSubArraySum(a, size))
    