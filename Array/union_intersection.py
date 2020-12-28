def get_union_intersection(arr1 , m , arr2 , n):
    i = j = 0
    union = [0] * (m+n)
    intersection = [0] * min(m , n)
    union_counter = 0
    intersection_counter = 0
    while i<m or j<n:
        if i==m:
            union[union_counter] = arr2[j]
            union_counter += 1
            temp = arr2[j]
            while j < n and arr2[j]==temp:
                j += 1
        elif j==n:
            union[union_counter] = arr1[i]
            union_counter += 1
            temp = arr1[i]
            while i < m and arr1[i]==temp:
                i += 1
        elif arr1[i] == arr2[j]:
            intersection[intersection_counter] = arr1[i]
            intersection_counter += 1
            union[union_counter] = arr1[i]
            union_counter += 1
            temp = arr2[j]
            while j < n and arr2[j]==temp:
                j += 1
            temp = arr1[i]
            while i < m and arr1[i]==temp:
                i += 1
        elif arr1[i] < arr2[j]:
            union[union_counter] = arr1[i]
            union_counter += 1
            temp = arr1[i]
            while i < m and arr1[i]==temp:
                i += 1
        else:
            union[union_counter] = arr2[j]
            union_counter += 1
            temp = arr2[j]
            while j < n and arr2[j]==temp:
                j += 1
            
    return union[:union_counter] , intersection[:intersection_counter]

print("Enter the array1 : ",end="")
arr1 = [int(x) for x in input().split()]
m = len(arr1)
print("Enter the array2 : ",end="")
arr2 = [int(x) for x in input().split()]
n = len(arr2)
union , intersection = get_union_intersection(arr1 , m , arr2 , n)
print("Union of two arrays : ",end="")
for i in union:
    print(i , end=" ")
print()
print("Intersection of two arrays : ",end="")
for i in intersection:
    print(i , end=" ")
print()