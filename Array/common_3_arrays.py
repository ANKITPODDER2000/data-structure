from get_array_helper import take_array_user
def common(arr1 , n1 , arr2 , n2 , arr3 , n3):
    i = j = k = 0
    while i<n1 and j < n2 and k < n3:
        # print(arr1[i] , arr2[j] , arr3[k])
        # print(i,j,k,n1,n2,n3)
        # print("-================================-")
        if arr1[i]==arr2[j] and arr2[j]==arr3[k]:
            print(arr1[i] , end=" ")
            i+=1
            j+=1
            k+=1
        elif arr1[i]>arr2[j]:
            j+=1
        elif arr2[j] > arr3[k]:
            k+=1
        else:
            i+=1
arr1 , n1 = take_array_user()
arr2 , n2 = take_array_user()
arr3 , n3 = take_array_user()
print("Common elements are : ",end="")
common(arr1 , n1 , arr2 , n2 , arr3 , n3)