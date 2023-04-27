import numpy as np
m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(0, m)]
k = [list(map(int, input().split())) for j in range(0, n)]
s = np.dot(l, k)
for i in range(0, len(s)):
    print(*s[i])
