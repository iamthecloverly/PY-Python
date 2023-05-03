i = 1
n = int(input())
for j in range(0,n):
    if(j == 1):
        i += n
        d = i-n
    elif(j == n-1):
        i = d
    for k in range(0,n):
        print(i,end="")
        if(k<n-1):
            print("*",end="")
        i += 1
    print()