n=int(input())
k=[[0 for j in range(0,n)] for i in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0):
            k[i][j]=1
        elif(i!=0 and j!=0):
            k[i][j]=k[i-1][j]+k[i][j-1]+k[i-1][j-1]
print(k[n-1][n-1])