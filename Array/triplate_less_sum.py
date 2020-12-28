from get_array_helper import take_array_user
def count_less_triplate_sum(arr , n , SUM):
    arr.sort()
    count = 0
    for i in range(n-1 , 1 , -1):
        j = 0
        k = i-1
        while j<k:
            if arr[j]+arr[k] < SUM:
                count += 1
                j += 1
                k -= 1
            else:
                k -= 1
    return count
arr , n = take_array_user()
SUM = int(input("Enter the sum : "))
count = count_less_triplate_sum(arr , n , SUM)
print("Count of triplates : ",count)