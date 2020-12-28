import sys
def minDist(arr, n, x, y):
    i=0
    p=-1
    min_dist = sys.maxsize; 
      
    for i in range(n):  
      
        if(arr[i] ==x or arr[i] == y): 
            if(p != -1 and arr[i] != arr[p]): 
                min_dist = min(min_dist,i-p)
            p=i 
    if(min_dist == sys.maxsize): 
       return -1
    return min_dist 

arr = [int(x) for x in input().split()]
n = len(arr)
x = 36
y = 33
print(minDist(arr, n, x, y))

