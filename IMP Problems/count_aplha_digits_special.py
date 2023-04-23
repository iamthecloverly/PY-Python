n = input()
a,b,c = 0,0,0
for i in n:
    if i.isalpha() == 1:
        a = a + 1
    elif i.isnumeric() == 1:
        b = b + 1
    else:
        c = c+1
print(a,b,c)
