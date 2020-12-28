def subArraySum(arr, n, sum): 
    curr_sum = arr[0] 
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i-1: 
          
            curr_sum = curr_sum - arr[start] 
            start += 1
            
        if curr_sum == sum: 
            print ("%d %d"%(start+1, i) , end="") 
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
    print ("-1" , end="") 
    return 0
    
sum = 8
arr =[1,8]
n = len(arr)
subArraySum(arr, n, sum)