def dynamicArray(n, queries):
    last_ans = 0
    ans = []
    q = [[] for i in range(n)]
    for (infor , x ,y) in queries:
        ind = (x ^ last_ans) % n
        if infor == 1:
            q[ind].append(y)
        else:
            last_ans = q[ind][y % len(q[ind])]
            ans.append(last_ans)
    return ans

li = [
      [1,0,5],
      [1,1,7],
      [1,0,3],
      [2,1,0],
      [2,1,1]
]
res = dynamicArray(2 , li)
print(res)
