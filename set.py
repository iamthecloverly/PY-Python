s = set(map(str,input().split()))
t = set(map(str,input().split()))
if t.issubset(s) == 1:
    print('subset')
else:
    print('not a subset')
