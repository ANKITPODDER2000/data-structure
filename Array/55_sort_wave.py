from get_array_helper import take_array_user
def sort_wave(arr , n):
    for i in range(0 , n , 2):

        if arr[i]<arr[i-1] and i > 0:
            arr[i] , arr[i-1] = arr[i-1] , arr[i]
        
        if arr[i]<arr[i+1] and i<n-1:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]

arr , n = take_array_user()
print("Sorting in wave form .....")
sort_wave(arr , n)
print("Sorting done .....")
print("Array after sorting in wave form : ",arr)
