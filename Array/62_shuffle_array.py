from get_array_helper import take_array_user
from random import randint
def shuffle(arr , n):
    for i in range(n-1,-1,-1):
        temp = randint(0 , i)
        arr[temp],arr[i] = arr[i],arr[temp]

arr , n = take_array_user()
shuffle(arr , n)
print("Shuffle   array : ",arr)