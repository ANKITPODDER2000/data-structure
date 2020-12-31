#maximum sum such that no two elements are adjacent.
def findsum(arr , n):
    incl = arr[0]
    excl = 0
    excl_new = 0
    for i in range(1):
        excl_new = max(incl , excl)
        incl = excl + arr[i]
        excl = excl_new
    return max(incl , excl)