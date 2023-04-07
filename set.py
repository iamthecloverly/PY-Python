s = set(map(str,input().split()))
t = set(map(str,input().split()))
k = t.issubset(s)
if k == 1:
    print('subset')
else:
    print('not a subset')
