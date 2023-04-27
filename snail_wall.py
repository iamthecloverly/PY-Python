n = int(input())
k = 0
for i in range(1, n+1):
    k = k + 3
    if k >= n:
        k = k-2
        break
    else:
        k = k - 2
print(k)
