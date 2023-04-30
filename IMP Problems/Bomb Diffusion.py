n,k = list(map(int,input().split()))
l = list(map(int,input().split()))
msg = []
for i in range(0, len(l)):
    ls = l[i:] + l[:i]
    msg.append(sum(ls[1::]))
print(*msg)
