from get_array_helper import take_array_user
def isSumPossible(arr , n , SUM):
    c = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j] == SUM:
                print("Numbers : %d & %d"%(arr[i],arr[j]))
                c += 1
    if c == 0:
        print("No such pair found!")

arr , n = take_array_user()
isSumPossible(arr , n , int(input("Enter the sum : ")))