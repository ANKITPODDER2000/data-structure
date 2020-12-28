def hourglassSum(arr):
    import math
    max_ = math.inf * -1
    for i in range(4):
        for j in range(4):
            num = 0
            for k in range(i , i+3):
                for l in range(j, j+3):
                    if not (k==i+1 and (l==j or l==j+2)):
                        num += arr[k][l]
            if num > max_:
                max_ = num
            #print(num)
    return max_

li = [
      [-9 ,-9 ,-9 , 1, 1, 1 ],    
      [0 ,-9 , 0 , 4 ,3 ,2],
      [-9, -9 ,-9,  1 ,2 ,3],
      [0 , 0,  8 , 6 ,6 ,0],
      [0,  0 , 0 ,-2 ,0 ,0],
      [0 , 0 , 1 , 2, 4, 0]
  ]

max_ = hourglassSum(li)