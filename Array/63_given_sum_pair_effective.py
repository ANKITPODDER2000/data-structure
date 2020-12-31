from get_array_helper import take_array_user
def isSumPossible(arr , n , SUM):
    c = 0
    HASH = {}
    for i in range(n):
        diff = SUM - arr[i]
        if diff in HASH:
            print("Numbers : %d & %d"%(arr[i],diff))
            c += 1
        else:
            HASH[arr[i]] = 1
    if c == 0:
        print("No such pair found!")

arr , n = take_array_user()
isSumPossible(arr , n , int(input("Enter the sum : ")))