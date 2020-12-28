def max_sum(a,n):
    inital_sum = 0
    initial_ans = 0
    for i in a:
        inital_sum += i
    for i in range(n):
        initial_ans += i * a[i]
    copy_ans = initial_ans
    #print(copy_ans)
    for i in range(n-1):
        copy_ans = (copy_ans - inital_sum) + (a[i] * (n-1)) + a[i]
        #print(copy_ans)
        if copy_ans > initial_ans:
            initial_ans = copy_ans
    return initial_ans
        
        
a = [8,3,1,2]
n = len(a)
ans = max_sum(a, n)
print(ans)

# 8 3 2 8
# 3 1 2 8
# 0 1 2 3