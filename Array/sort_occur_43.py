from get_array_helper import take_array_user
def mod_sort(arr , n):
    # print(arr)
    for i in range(n-1):
        for j in range(0 , n-i-1):
            if arr[j][0]<arr[j+1][0] or (arr[j][0]==arr[j+1][0] and arr[j][2]>arr[j+1][2]):
                arr[j+1] , arr[j] = arr[j] , arr[j+1]
def get_sorted_arr(arr , n):
    HASH = {}
    for i in range(n):
        if arr[i] not in HASH:
            HASH[arr[i]] = {}
            HASH[arr[i]]["count"] = 0
            HASH[arr[i]]["index"] = i
            HASH[arr[i]]["val"] = arr[i]
        HASH[arr[i]]['count'] += 1
    array = [[0 , 0 ,0] for i in range(len(HASH))] #[[count ,val , ind]]
    c = 0
    for i in HASH:
        array[c][0] = HASH[i]["count"]
        array[c][1] = i
        array[c][2] = HASH[i]["index"]
        c+=1
    mod_sort(array , len(array))
    print("Sorted arr(w.r.t occurence) : ",end="")
    for i in array:
        for j in range(i[0]):
            print(i[1],end=" ")

arr , n = take_array_user()
get_sorted_arr(arr , n)