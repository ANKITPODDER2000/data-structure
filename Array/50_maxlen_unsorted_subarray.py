from get_array_helper import take_array_user
import math
def maxlen_unsortedarray(arr , n):
    l = r = None
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            l = i
            break
    if l == None:
        return False
    for i in range(n-1 , 0 , -1):
        if arr[i]<arr[i-1]:
            r = i
            break
    MAX = math.inf * -1
    MIN = math.inf 
    for i in range(l , r+1):
        MAX = max(MAX , arr[i])
        MIN = min(MIN , arr[i])
    
    i = l-1
    while i>=0 and arr[i]>MIN:
        i -= 1
    l = i+1

    i = r+1
    while i<n and arr[i]<MAX:
        i+=1
    r = i-1

    print("Minimum lenght of unsorted array is : ",r-l+1)
arr , n = take_array_user()
maxlen_unsortedarray(arr , n)

