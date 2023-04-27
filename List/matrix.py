# Program to get the matrix elements

k = int(input())
n = int(input())
l = [[int(input()) for j in range(0, n)] for i in range(0, k)]
for i in range(0, k):
    for j in range(0, n):
        print(l[i][j], end=" ")
    print()
