from get_array_helper import take_array_user
def is_sum_possible(arr , n , sum):
    Hash = {}
    for i in arr:
        temp = sum - i
        if temp in Hash:
            return True
        Hash[i] = True
    return False
arr , n = take_array_user()
sum = int(input("Enter the sum : "))
isPossible = is_sum_possible(arr , n , sum)
print("Get the sum by add two numbers : ",isPossible)