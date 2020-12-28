from get_array_helper import take_array_user
def loss_element(arr1 , arr2):
    loss = 0
    for i in arr1:
        loss = loss ^ i
    for i in arr2:
        loss = loss ^ i
    return loss

arr1 , _ = take_array_user("Enter the array1")
arr2 , _ = take_array_user("Enter the array2")
loss     = loss_element(arr1 , arr2)
print("Loss element is : ",loss)