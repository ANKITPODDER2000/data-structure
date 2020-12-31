from get_array_helper import take_array_user
def print_triplates(arr , n , SUM):
    arr.sort()
    for i in range(n-1 , 1 , -1):
        l = 0
        r = i-1
        while l<r:
            if arr[l]+arr[r]+arr[i] == SUM:
                print("Values of triplates with %d sum : %d %d and %d"%(SUM,arr[l],arr[r],arr[i]))
                l+=1
                r-=1
            elif arr[l]+arr[r]+arr[i] - SUM>0:
                r-=1
            else:
                l+=1
arr , n = take_array_user()
print_triplates(arr , n ,int(input("Enter sum : ")))