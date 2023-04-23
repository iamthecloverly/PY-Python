n = input()
l = ['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i in l:
        x = n.replace(i,"_",1)
        break
print(x)
