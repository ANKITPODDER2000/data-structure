def reverseArray(a):
    l = len(a)
    for i in range(l//2):
        a[i] , a[l-1-i] = a[l-1-i] , a[i]
    return a

a = reverseArray([1,2,3,5])
print(a)