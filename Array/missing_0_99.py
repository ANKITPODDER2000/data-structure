from get_array_helper import take_array_user
def print_missings(arr , n):
    track = [0] * 100
    for i in range(n):
        if 0 <= arr[i] and arr[i]<=99:
            track[arr[i]] = 1
    print("Missing values are : ")
    if track[0]==0:
        print(0,"- ",end="")
    for i in range(1 , 99):
        if track[i]==0 and track[i-1]==1:
            print(i,"- ",end="")
        if track[i]==0 and track[i+1]==1:
            print(i)
    if track[-1]==0:
        print(99)
arr , n = take_array_user()
print_missings(arr , n)
