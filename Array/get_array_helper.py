def take_array_user(string="Enter the array"):
    print(string+" : " , end="")
    arr = [int(x) for x in input().split(" ")]
    return arr , len(arr)