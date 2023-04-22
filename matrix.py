n=int(input())
k=[[map(int,input().split()) for j in range(0,n)] for i in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        print(k[i][j],end=" ")
    print()