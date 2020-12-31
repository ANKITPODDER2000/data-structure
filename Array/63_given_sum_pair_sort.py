from get_array_helper import take_array_user
def isSumPossible(arr , n , SUM):
    c = 0
    arr.sort()
    l = 0
    r = n-1
    while l<r:
        if arr[l]+arr[r] == SUM:
            print("Numbers : %d & %d"%(arr[l],arr[r]))
            c += 1
            l+=1
            r-=1
        elif arr[l]+arr[r] > SUM:
            r -= 1
        else:
            l+=1
    if c == 0:
        print("No such pair found!")

arr , n = take_array_user()
isSumPossible(arr , n , int(input("Enter the sum : ")))