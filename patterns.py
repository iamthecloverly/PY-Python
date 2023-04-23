n = int(input())
for i in range(0, n):
    for j in range(0, n):
        if i+j >= n-1:
            print(n-j, end="")
        else:
            print(" ", end="")
    print()
