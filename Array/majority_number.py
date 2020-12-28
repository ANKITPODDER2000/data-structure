def get_prob_majority_number(arr , n):
    num   = arr[0]
    count = 1
    for i in range(1,n):
        if arr[i]==num:
            count += 1
        else:
            count -= 1
        if count == 0:
            count = 1
            num   = arr[i]
    return num
def get_majority_numer(arr , n):
    num   = get_prob_majority_number(arr , n)
    count = 0
    for i in range(n):
        if arr[i]==num:
            count += 1
    if count > (n//2):
        return num
    else:
        return None
print("Enter the array : ",end="")
arr = [int(x) for x in input().split()]
ans = get_majority_numer(arr , len(arr))
print("Majority number is : ",ans)