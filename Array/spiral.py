def spiral(arr , r1 , r2 , c1 , c2):
    if r1>r2 or c1>c2:
        return False
    for i in range(c1,c2+1):
        print(arr[r1][i] , end=" ")
    for i in range(r1+1 , r2+1):
        print(arr[i][c2],end=" ")
    for i in range(c2-1 , c1-1 , -1):
        print(arr[r2][i] , end=" ")
    for i in range(r2-1 , r1 , -1):
        print(arr[i][c1],end=" ")
    spiral(arr , r1 +1 , r2 - 1 , c1 +1 , c2-1)

r,c = input("Enter the row and collum : ").split(" ")
r , c = int(r) , int(c)
matrix = []
print("Enter the matrix : ")
for i in range(r):
    temp = [int(x) for x in input().split(" ")]
    matrix.append(temp)
print("Spiral of matrix : ",end=" ")
spiral(matrix , 0 , r-1 , 0 , c-1)