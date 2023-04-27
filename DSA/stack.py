a = []
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print(a)
a.pop()
print(a)

for i in range(len(a)-1, -1, -1):
    a[i] = a[i] + 1
    if a[i] < 9:
        break
    else:
        a[i] = 0
print(a)