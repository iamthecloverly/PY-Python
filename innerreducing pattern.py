n = int(input())
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        print(n-min(i,j,(2*n-2)-i,(2*n-2)-j),end=" ")
    print() 