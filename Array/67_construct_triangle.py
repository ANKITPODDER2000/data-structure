from get_array_helper import take_array_user
def display(arr , n):
    for i in range(n):
        for j in range(i+1):
            print("%3d"%arr[i][j] , end=" ")
        print()
def construct_array(arr , n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        matrix[-1][i] = arr[i]
    for i in range(n-2 , -1 , -1):
        for j in range(i+1):
            matrix[i][j] = matrix[i+1][j] + matrix[i+1][j+1]
    display(matrix , n)
arr , n = take_array_user()
construct_array(arr , n)