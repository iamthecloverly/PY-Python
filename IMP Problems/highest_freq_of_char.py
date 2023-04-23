n = input()
max = 0
for i in n:
    if n.count(i) > max:
        max = n.count(i)
        d = i
print(d)
