n = int(input())
dict = {}
for i in range(0,n):
    key,values = map(str,input().split())
    dict[key] = values
print(dict.fromkeys(dict['ajay']))
