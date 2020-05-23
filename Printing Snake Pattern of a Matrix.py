
def snakepattern(matrix,m,n):
    for i in range(m):
        if(i%2==0):
            for j in range(n):
                print(str(matrix[i][j]),end=" ")
        else:
            for j in range(n-1,-1,-1):
                print(str(matrix[i][j]),end=" ")

m,n = map(int,input().split(" "))
#print(m,n)
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    matrix.append(row)
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()
snakepattern(matrix,m,n)
