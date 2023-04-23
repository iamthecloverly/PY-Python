n = input()
a,b = 0,0
l = ['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i not in l:
        a = a+1
    else:
        b = b+1
print("Vowels",b)
print("Consonants",a)