from get_array_helper import take_array_user
def equi(arr , n):
    s = sum(arr)
    l_sum = 0
    for i in range(n):
        r_sum = s-arr[i]-l_sum
        if l_sum == r_sum:
            print("Equilibrium index is : %d"%i)
        l_sum = l_sum + arr[i]
arr , n = take_array_user()
equi(arr , n)