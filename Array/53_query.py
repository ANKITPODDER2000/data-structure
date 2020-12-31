from get_array_helper import take_array_user
#use binary search for better solution
def query(arr,n,q,x):
    n = n
    count = 0
    if q==0:
        for i in arr:
            if i>=x:
                count += 1
    else:
        for i in arr:
            if i>x:
                count += 1
    return count

arr , n = take_array_user()
for i in range(2):
    q , x = input().split(" ")
    q , x = int(q) , int(x)
    print("count = %d"%query(arr , n , q , x))