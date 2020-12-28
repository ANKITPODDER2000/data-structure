import sys
def get_minimum_distance(arr , n , x, y):
    prev = -1
    min_distance = sys.maxsize
    for i in range(0 , n):
        if arr[i] == x or arr[i]==y:
            if prev == -1:
                prev = i
            elif arr[prev] != arr[i]:
                l = i - prev
                if l < min_distance:
                    min_distance = l
                prev = i
    if min_distance == sys.maxsize:
        return "Infinite"
    return min_distance

print("Enter the array : ",end="")
arr = [int(x) for x in input().split()]
n = len(arr)
x , y = input("Enter x and y : ").split(" ")
x , y = int(x) , int(y)
ans = get_minimum_distance(arr , n , x , y)
print("Minimum distance is : ",ans)