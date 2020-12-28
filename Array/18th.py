def firstRepeated(arr, n):
    hashmap = {}
    for i in arr:
        if i not in hashmap:
            hashmap[i] = 0
        hashmap[i] += 1
    for i in range(n):
        if hashmap[arr[i]] >1:
            return i+1
    return -1

arr = [1, 5,4,3]
n   = len(arr)
print(firstRepeated(arr, n))